"""
QUESTION:
Write a function called `is_valid_ipv4_address` that takes a string `ip_str` as input and checks if it is a valid IPv4 address. The function should return `True` if the input string is a valid IPv4 address and `False` otherwise. Additionally, the function should also check if the given IPv4 address belongs to a reserved network range and return a string indicating the type of network range it belongs to: "Global Unicast" if the IP address belongs to a globally routable network, "Private Use" if the IP address belongs to a private network range, "Reserved" if the IP address belongs to a reserved network range, and "Unknown" if the IP address does not belong to any of the specified network ranges. The function should handle error cases where the input string is not a valid IP address.
"""

import ipaddress

def is_valid_ipv4_address(ip_str):
    try:
        # Parse the IP address string
        ip = ipaddress.ip_interface(ip_str)
        
        # Check if the IP address is IPv4
        if ip.version == 4:
            # Check if the IP address belongs to a reserved network range
            if ip.is_global:
                network_range_type = "Global Unicast"
            elif ip.is_private:
                network_range_type = "Private Use"
            elif ip.is_reserved:
                network_range_type = "Reserved"
            elif ip.is_multicast:
                network_range_type = "Multicast"
            else:
                network_range_type = "Unknown"
            
            return (True, network_range_type)
    except ValueError:
        pass
    
    return (False, "Invalid IP Address")