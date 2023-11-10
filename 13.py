from ipaddress import *

for mask in range(33):
    net1 = ip_network(f'140.37.235.224/{mask}', False)
    net2 = ip_network(f'140.37.235.192/{mask}', False)

    if net1.network_address == net2.network_address:
        print(net1.netmask)
