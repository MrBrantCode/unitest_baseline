"""
QUESTION:
Write a function `get_subnet_mask` that takes an IP address and subnet prefix as input and returns the subnet mask associated with the IP address. The function should use Python's `IPv4Network` library and the input should be in CIDR notation (x.x.x.x/y), where y denotes the number of bits used for the network part of the address.
"""

from ipaddress import IPv4Network

def get_subnet_mask(ip_address):
    """
    Returns the subnet mask associated with the given IP address and subnet prefix.

    Args:
        ip_address (str): IP address in CIDR notation (x.x.x.x/y)

    Returns:
        str: Subnet mask associated with the IP address
    """
    net = IPv4Network(ip_address)
    return str(net.netmask)