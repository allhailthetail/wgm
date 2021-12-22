import wgkey
import os, sys

def newclient(hostname, clientname, client_ip, host_endpoint, allowed_ip, dns, host_endpoint_port):
    
    '''
    Responsible creating a new "client" interface, 
    writing the host-side interface to /etc/wireguard/host.d/client.host.conf,
    writing the client-side interface to /etc/wireguard/host.d/client.conf,
    and saving the client private key to /etc/wireguard/host.d/client.host.private.
    '''

    # replace default values if passed a None type:
    if dns == None:
        dns='8.8.8.8'
    if host_endpoint_port == None:
        host_endpoint_port=51820
    
    # crash if missing this paramenter.  Must be provided!
    if allowed_ip == None:
        sys.exit('must specify allowed ip(s} for client!!')
    
    # call wgkey.genkey to fetch a unique keypair
    KeyPair = wgkey.genkeys()

    # verify valid hostname exists
    os.path.isdir(f'/etc/wireguard/{hostname}.d/')
    os.path.isfile(f'/etc/wireguard/{hostname}.d/{hostname}.host.conf')
    
    # create client.* files:
    with open(f'/etc/wireguard/{hostname}.d/{clientname}.{hostname}.conf', 'w') as f:       # hostfile in drop directory
        f.writelines([
            f'#{clientname}.{hostname}.conf\n',
            f'[Peer]\n',
            f"PublicKey = {KeyPair['pubkey']}\n",                                           # PUBLIC KEY OF CLIENT
            f'AllowedIPs = {allowed_ip}\n',
            f'PersistentKeepalive = 25'
        ])
        f.close()
    with open(f'/etc/wireguard/{hostname}.d/{clientname}.conf', 'w') as f:                  # hostfile in drop directory
        f.writelines([
            f'[Interface]\n',
            f"PrivateKey = {KeyPair['privkey']}\n",                                         # client private key
            f'Address = {client_ip}\n',                                                     # tunnel IP client will receive
            f'DNS = {dns}\n',                                                               # DNS servers client will use
            f'\n\n[Peer]\n',
            f'PublicKey = {wgkey.get_host_public(hostname)}\n',                             # host interface public key        
            f'Endpoint = {host_endpoint}:{host_endpoint_port} \n',                          # host WAN address : listening port
            f'AllowedIPs = {allowed_ip}\n'                                                  # scope of accessible addresses for tunnel
                                                                                                # 0.0.0.0/0 makes tunnel default gateway
        ])
        f.close()
    with open(f'/etc/wireguard/{hostname}.d/{clientname}.{hostname}.private', 'w') as f:    # client private key
        f.write(f"{KeyPair['privkey']}\n")
        f.close()