import library.wgkey
import os

def newhost(hostname, ip_cidr, listenport):
    '''
    Responsible for creating a new "host" interface,
    writing the interface to /etc/wireguard/.conf 
    and backing up a copy to /etc/wireguard/hosts/.conf.bak
    '''

    # replace default values if passed a None type:
    if hostname == None:
        hostname = 'wg0'
    if ip_cidr == None:
        ip_cidr = '10.0.0.1/24'
    if listenport == None:
        listenport = 51820
        
    # PLACEHOLDER VALUES, REPLACE LATER!!
    PostUp = '#/etc/wireguard/PostUp.sh'
    PostDown = '#/etc/wireguard/PostDown.sh'
    
    # call lib.wgkey.genkey to fetch public/private pair
    KeyPair = library.wgkey.genkeys()

    # create directory hostname.d
    # write new file, hostname.host.conf
    # write new file, hostname.private
    os.mkdir(f'/etc/wireguard/{hostname}.d')
    with open(f'/etc/wireguard/{hostname}.d/{hostname}.host.conf', 'w') as f:     # hostfile in drop directory
                f.writelines([
                    f'#{hostname}.host.conf\n',
                    '[Interface]\n',
                    f"PrivateKey = {KeyPair['privkey']}\n",
                    f'Address = {ip_cidr}\n',
                    f'ListenPort = {listenport}\n',
                    f'PostUp = {PostUp}\n',
                    f'PostDown = {PostDown}\n'
                ])
                f.close()
    with open(f'/etc/wireguard/{hostname}.d/{hostname}.private', 'w') as f:       # create .private containing private key
        f.write(f"{KeyPair['privkey']}\n")
        f.close()