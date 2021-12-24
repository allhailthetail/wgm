import ipaddress

# usable client addresses is total - 2
def max_usable_hosts(addr):
    return ipaddress.ip_network(addr).num_addresses - 2

def get_host_list(addr):
    return ipaddress.ip_network(addr).hosts()




print(max_usable_hosts('10.0.0.0/32'))

print(list(get_host_list('10.0.0.0/32')))

# print(ipaddress.ip_network('10.0.0.0/24').num_addresses)