import subprocess

def genkeys(name, path):
    
    """
    Generate a WireGuard private & public key
    Requires that the 'wg' command is available on PATH
    Returns (private_key, public_key), both strings
    """
    
    # define new variable:
    KeyPair = {'privkey':'', 'pubkey':''}

    # fill values:
    KeyPair['privkey'] = subprocess.check_output("wg genkey", shell=True).decode("utf-8").strip()
    privkey = KeyPair['privkey']
    KeyPair['pubkey'] = subprocess.check_output(f"echo '{privkey}' | wg pubkey", shell=True).decode("utf-8").strip()
    
    with open(f'{path+name}.public', 'w') as f:     # write public key
                f.write(f"{KeyPair['pubkey']}\n")
                f.close()

    with open(f'{path+name}.private', 'w') as f:    # write private key
                f.write(f"{KeyPair['privkey']}\n")
                f.close()
    
    # return keypair back to program for further processing:
    return(KeyPair)