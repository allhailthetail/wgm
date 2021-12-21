from shutil import copyfile
import library.wgkey
# from wgkey import genkeys

# global static: ../hosts location:
hosts_dir = '/etc/wireguard/hosts/'
main_cfg_dir = '/etc/wireguard/'

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
    
    # call lib.wgkey.genkey to fetch values for function
    #   and save those values for future use:
    KeyPair = library.wgkey.genkeys(hostname, hosts_dir)

    with open(f'/etc/wireguard/{hostname}.conf', 'w') as f:     # write /etc/wireguard/.conf
                f.writelines([
                    '## CREATED AUTOMATICALLY WITH WGWIZ\n',
                    '## DO NOT EDIT DIRECTLY!!\n\n',
                    f'# Name: {hostname}\n',
                    '[Interface]\n',
                    f"PrivateKey = {KeyPair['privkey']}\n",
                    f'Address = {ip_cidr}\n',
                    f'ListenPort = {listenport}\n',
                    f'PostUp = {PostUp}\n',
                    f'PostDown = {PostDown}\n'
                ])
                f.close()

    # backup newly-created file to /etc/wireguard/hosts/.conf.bak
    copyfile(f'/etc/wireguard/{hostname}.conf', f'/etc/wireguard/hosts/{hostname}.conf.bak')