import wgm.wgkey
import os, sys

def newclient(hostname, clientname, client_ip, host_endpoint, allowed_ip, dns, host_endpoint_port):
    
    '''
    Responsible for verifying valid input at runtime, filling for optional/implied values,
    verifying valid configuration,
    creating a new "client" interface and accompanying files.
    '''

    # replace default values if passed a None type:
    if dns == None:
        dns='8.8.8.8'
    if host_endpoint_port == None:
        host_endpoint_port=51820
    
    # crash if missing this paramenter.  Must be provided!
    if allowed_ip == None:
        sys.exit('must specify allowed ip(s} for client!!')
    
    # call lib.wgkey.genkey to fetch public/private pair
    KeyPair = wgm.wgkey.genkeys()

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
            f"PrivateKey = {KeyPair['privkey']}\n",
            f'Address = {client_ip}\n',                        
            f'DNS = {dns}\n',
            f'\n\n[Peer]\n',
            f'PublicKey = {wgm.wgkey.get_host_public(hostname)}\n',                                     
            f'Endpoint = {host_endpoint}:{host_endpoint_port} \n',  
            f'AllowedIPs = {allowed_ip}\n'
        ])
        f.close()
    with open(f'/etc/wireguard/{hostname}.d/{clientname}.{hostname}.private', 'w') as f:    # create .private containing private key
        f.write(f"{KeyPair['privkey']}\n")
        f.close()