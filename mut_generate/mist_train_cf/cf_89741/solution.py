"""
QUESTION:
Write a function `is_valid_ipv4_address(ip_str)` that takes a string as input and checks if it is a valid IPv4 address. The function should return `True` if the input string is a valid IPv4 address and `False` otherwise. Additionally, the function should also check if the given IPv4 address belongs to a reserved network range and return a string indicating the type of network range it belongs to: "Global Unicast" if the IP address belongs to a globally routable network, "Private Use" if the IP address belongs to a private network range, "Reserved" if the IP address belongs to a reserved network range, and "Unknown" if the IP address does not belong to any of the specified network ranges. The function should support IPv4 addresses in standard notation (e.g., "192.168.0.1") and should not support IPv6 addresses or CIDR notation.
"""

import ipaddress

def is_valid_ipv4_address(ip_str):
    try:
        ip = ipaddress.ip_interface(ip_str)
        
        if ip.version == 4:
            if ip.is_global:
                return "Global Unicast"
            elif ip.is_private:
                return "Private Use"
            elif ip.is_reserved:
                return "Reserved"
            elif ip.is_multicast:
                return "Multicast"
            else:
                return "Unknown"
    except ValueError:
        pass
    
    return False