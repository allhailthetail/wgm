def warn_no_root():
    print("This Utility Must be ran with admin privileges!")

def panic_exit():
    print("Program panic!!  exiting...")

def warn_invalid_option():
    print("Invalid option entered!!")

def manpage():
    print('''
    
    NAME
        wgwiz - WireGuard Wizard
        
    SYNOPSIS
        wgwiz [-option] [--option] <args> ...
    
    DESCRIPTION
        The wgwiz program assists in the creation of WireGuard connections in a host-client configuration.
        This tool aims to de-mystify the setup of one-to-oen and one-to-multiple connections between hosts
        by organizing otherwise loosely-associated keypairs and configuration files.  
        Administrative privileges are required in order to use this program.  
    
    Options
        -N, --newhost <hostname> <ip addr/CIDR>
            * Create a new host interface, hostname.conf in /etc/wireguard/
        
        -n, --new-client <hostname> <clientname>
            * Create a new client in /etc/wireguard/clients/hostname.d/ 
            * append host to /etc/wireguard/hostname.conf
        
        -i, --interactive
            Interactive mode
    
    FILES
        /etc/wireguard/<hostname.conf>
            each file represents 'host-side, root' interface configuration.

        /etc/wireguard/clients/<hostname.d>
            each hostname.d folder contains groupings of clients by their connection to 
            a given host interface

        /etc/wireguard/clients/<hostname.d>/<clientname>
            contains clientname.conf and public/private keypairs
    
    ''')

