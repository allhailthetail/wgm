import wgkey
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
    # can a single firewall.d zone handle the whole thing?  simple on and off?
    PostUp = '#/etc/wireguard/PostUp.sh'
    PostDown = '#/etc/wireguard/PostDown.sh'
    
    # call lib.wgkey.genkey to fetch a unique pair
    KeyPair = wgkey.genkeys()

    # create hostname.* files
    os.mkdir(f'/etc/wireguard/{hostname}.d')
    with open(f'/etc/wireguard/{hostname}.d/{hostname}.host.conf', 'w') as f:     # hostfile in drop directory
                f.writelines([
                    f'#{hostname}.host.conf\n',
                    f"#PublicKey = {KeyPair['pubkey']}\n\n"
                    '[Interface]\n',
                    f"PrivateKey = {KeyPair['privkey']}\n",                       # private key of host interface
                    f'Address = {ip_cidr}\n',                                     # public-facing WAN address
                    f'ListenPort = {listenport}\n',                               # port wireguard listens for connections
                    f'PostUp = {PostUp}\n',                                       # firewall script to run on initialization
                    f'PostDown = {PostDown}\n'                                    # firewall script to run on shutdown
                ])
                f.close()