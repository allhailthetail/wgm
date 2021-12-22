import wgkey
import os

def newclient(hostname, clientname, allowed_ip, host_endpoint, host_endpoint_port=51820):
    '''
    Responsible for creating a new "host" interface,
    writing the interface to /etc/wireguard/.conf 
    and backing up a copy to /etc/wireguard/hosts/.conf.bak
    '''

    # replace default values if passed a None type:
    if clientname == None:
        clientname = 'cl1'
    
    # call lib.wgkey.genkey to fetch public/private pair
    KeyPair = wgkey.genkeys()

    # navigate to host.d/
    # write new file, client.host.conf
    # write new file, client.conf
    # write new file, client.host.private
    os.path.isdir(f'/etc/wireguard/{hostname}.d/')
    os.path.isfile(f'/etc/wireguard/{hostname}.d/{hostname}.host.conf')
    with open(f'/etc/wireguard/{hostname}.d/{clientname}.{hostname}.conf', 'w') as f:     # hostfile in drop directory
                f.writelines([
                    f'#{clientname}.{hostname}.conf\n',
                    f'[Peer]\n',
                    f"PublicKey = {KeyPair['pubkey']}\n",                  #PUBLIC KEY OF CLIENT
                    f'AllowedIPs = {allowed_ip}\n',
                    f'PersistentKeepalive = 25'
                ])
                f.close()
    with open(f'/etc/wireguard/{hostname}.d/{clientname}.conf', 'w') as f:     # hostfile in drop directory
                f.writelines([
                    f'[Interface]\n',
                    f"PrivateKey = {KeyPair['privkey']}\n",
                    f'Address = {allowed_ip}\n',                        
                    f'DNS = 8.8.8.8\n',
                    f'\n\n[Peer]',
                    f'PublicKey = ',                                         # new function, grab public from host.private
                    f'Endpoint = {host_endpoint}:{host_endpoint_port} \n',  
                    f'AllowedIPs = 0.0.0.0/0'
                ])
                f.close()
    with open(f'/etc/wireguard/{hostname}.d/{clientname}.{hostname}.private', 'w') as f:       # create .private containing private key
        f.write(f"{KeyPair['privkey']}\n")
        f.close()



# for debugging:
newclient('wg0', None)