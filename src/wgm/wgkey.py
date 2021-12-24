import subprocess, os

def genkeys():
    
    """
    Generate a WireGuard private & public key
    Requires that the 'wg' command is available on PATH
    Returns (private_key, public_key), both strings
    """
    
    KeyPair = {'privkey':'', 'pubkey':''}

    # fill values:
    KeyPair['privkey'] = subprocess.check_output("wg genkey", shell=True).decode("utf-8").strip()
    privkey = KeyPair['privkey']
    KeyPair['pubkey'] = subprocess.check_output(f"echo '{privkey}' | wg pubkey", shell=True).decode("utf-8").strip()

    # return keypair back to program for further processing:
    return(KeyPair)

def get_host_private(hostname):
    """
    Parses hostname.host.conf and returns its private key.  
    This elliminates the need to have a separate file just to hold a .private file. 
    """
    with open(f'/etc/wireguard/{hostname}.d/{hostname}.host.conf', 'rt') as f:
        lines = f.readlines()

    for line in lines:
        if 'PrivateKey' in line:
            priv = line.replace('PrivateKey = ', '')
            break
    return priv.replace('\n','')

def get_host_public(hostname):
    """
    Parses hostname.host.conf and returns its private key.  
    This elliminates the need to have a separate file just to hold a .private file. 
    """
    with open(f'/etc/wireguard/{hostname}.d/{hostname}.host.conf', 'rt') as f:
        lines = f.readlines()

    for line in lines:
        if 'PublicKey' in line:
            pub = line.replace('#PublicKey = ', '')
            break
    return pub.replace('\n','')