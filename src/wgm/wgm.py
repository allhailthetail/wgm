import os, sys, subprocess, argparse
import newhost, newclient

def is_root():
    if os.geteuid() == 0:
        return True
    else:
        return False

def main():

    # Check if root before continuing:
    if is_root():
        parser = argparse.ArgumentParser(description='wgwiz utility:')

        parser.add_argument('-N', '--newhost',
            dest='HOSTNAME',
            help='Create a new host interface, <hostname>.conf')

        parser.add_argument('-n', '--newclient', 
            dest='CLIENTNAME',
            help='Create a new host interface, <clientname>.conf')

        parser.add_argument('-p', '--port',
            dest='PORT',
            help='Specify port for host or client')

        parser.add_argument('-I', '--ip-host',
            dest='IP_HOST',
            help='Specify host IPv4 Address x.x.x.x/x in CIDR')
        
        parser.add_argument('-i', '--ip',
            dest='IP',
            help='Specify target IPv4 Address x.x.x.x/x in CIDR')
        
        parser.add_argument('-b', '--bind-to',
            dest='BIND_TO',
            help='tell client which host to bind to')

        parser.add_argument('-e','--endpoint',
            dest='ENDPOINT',
            help='tell client public host address')
        
        parser.add_argument('--allowed',
            dest='ALLOWED',
            help='allowed addresses')
        
        parser.add_argument('--dns',
            dest='DNS',
            help='specify DNS Nameservers')

        args = parser.parse_args()

        # cannot create host and client in one line, exit
        if args.HOSTNAME and args.CLIENTNAME:
            sys.exit('hosts and clients must be created separately!!')

        # create new 'host' WireGuard interface
        if args.HOSTNAME:                            
            newhost.newhost(
                hostname=args.HOSTNAME, 
                ip_cidr=args.IP, 
                listenport=args.PORT)   
        
        # create new 'client' WireGuard interface
        if args.CLIENTNAME:
            newclient.newclient(
                hostname = args.BIND_TO,
                clientname=args.CLIENTNAME,
                client_ip=args.IP,
                host_endpoint = args.ENDPOINT,
                #Allowed has a problem, allows match on client and server!
                #This should be different between the two!
                allowed_ip=args.ALLOWED,
                dns = args.DNS,
                host_endpoint_port = args.PORT
            )
    
    # If not root,
    else: 
        sys.exit('must run as root!!')




if __name__== "__main__":
    main()