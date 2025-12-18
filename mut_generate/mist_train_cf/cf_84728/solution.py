"""
QUESTION:
Design a function called `calculate_subnet` that calculates the subnet mask for a given IP address and CIDR value. The function should take two parameters: an IP address in dotted decimal format and a CIDR value, and return the subnet mask in dotted decimal format. Implement error handling to handle invalid IP addresses. The function should only work with IPv4 addresses.
"""

import ipaddress

def calculate_subnet(ip, cidr):
    try:
        network = ipaddress.IPv4Network(f'{ip}/{cidr}', strict=False)
    except ValueError as e:
        return str(e)
    
    return str(network.netmask)