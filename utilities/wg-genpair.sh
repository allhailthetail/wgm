# Script Invented by Matthew,
# prints wireguard pairs with a single command:

#!/bin/bash
private_key=$(wg genkey)
public_key=$(echo $private_key | wg pubkey)
echo -e "\nprivate key:" 
echo -e "$private_key\n"
echo -e "public key:"
echo -e "$public_key\n"
