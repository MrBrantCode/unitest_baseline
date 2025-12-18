"""
QUESTION:
Create a function `get_network_address(ip, mask)` that takes an IP address and a subnet mask as arguments and returns the network address. The function should be compatible with both IPv4 and IPv6 addresses.

Create another function `cidr_contains_ip(cidr, host)` that checks whether a given IP address belongs to a specific network based on a provided CIDR block. The function should also be compatible with both IPv4 and IPv6 addresses.

The functions should not require any additional libraries beyond the Python standard library, specifically the `ipaddress` module.
"""

import ipaddress

def get_network_address(ip, mask):
    """
    This function gives the network address. It's compatible with IPv4 and IPv6.
    """
    net = ipaddress.ip_interface(f'{ip}/{mask}')
    return net.network.network_address

def cidr_contains_ip(cidr, host):
    """
    This function will identify whether a supplied IP address belongs to a given network 
    based on provided CIDR block for both IPv4 and IPv6 addresses.
    """
    return ipaddress.ip_address(host) in ipaddress.ip_network(cidr)