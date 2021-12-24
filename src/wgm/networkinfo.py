import ipaddress

# usable client addresses is total - 2
def max_usable_hosts(addr):
    """
    compute total number of client connections
    that can be made with a given network
    """
    return ipaddress.ip_network(addr).num_addresses - 2

def get_host_list(addr):
    """
    give a range of available client and host addresses,
    """
    return ipaddress.ip_network(addr).hosts()