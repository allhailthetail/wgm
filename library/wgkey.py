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

def get_host_public(hostname):
    """
    processes the host.private file and returns the corresponding public key 
    """
    os.path.isdir('/etc/wireguard/{hostname}.d/')
    os.path.isfile('/etc/wireguard/{hostname.d/{hostname}.private')
    return subprocess.check_output(f'wg pubkey < /etc/wireguard/{hostname}.d/{hostname}.private', shell=True).decode('utf-8').strip()