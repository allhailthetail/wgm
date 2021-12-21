import os, sys

# global static: ../hosts location:
hosts_dir = '/etc/wireguard/hosts/'
main_cfg_dir = '/etc/wireguard/'


## Function creates a new host:
def newhost(hostname='wg0', ip_cidr='10.0.0.0/24', listenport=51820):

    # Check if ../hosts folder exists.  Continue 
    if os.path.exists(hosts_dir):
        # Check if ../hosts/.conf already exists.  Exit
        if os.path.exists(hosts_dir+hostname+'.conf'):
            sys.exit(f"{hostname}.conf Already Exists!!  Terminating...")
        
        # if does not exist, create
        else:
            #replace later!
            privatekey = 'test'
            with open(f'{hosts_dir+hostname}.conf.backup', 'w') as f:
                f.writelines([
                    f'#{hostname}.conf\n',
                    '[Interface]\n',
                    f'PrivateKey = {privatekey}\n',
                    f'Address = {ip_cidr}\n',
                    f'ListenPort = {listenport}\n'
        ])
    #if ../hosts does not exist, terminate with error
    else:
        sys.exit('/etc/wireguard/hosts does not exist!!  Terminating...')

    if os.path.exists(main_cfg_dir+hostname+'.conf'):
        sys.exit(f"{main_cfg_dir+hostname}.conf Already Exists!!  Terminating...")
    else:
        #replace later!
            privatekey = 'test'
            with open(f'{main_cfg_dir+hostname}.conf', 'w') as f:
                f.writelines([
                    '## CREATED AUTOMATICALLY WITH WGWIZ\n',
                    '## DO NOT EDIT DIRECTLY!!\n\n',
                    f'#{hostname}.conf Main Configuration File:\n',
                    '[Interface]\n',
                    f'PrivateKey = {privatekey}\n',
                    f'Address = {ip_cidr}\n',
                    f'ListenPort = {listenport}\n'
                ])


newhost('testinterface')