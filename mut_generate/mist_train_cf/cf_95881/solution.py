"""
QUESTION:
Write a function named `is_valid_ip_address` that checks if a given string is a valid IP address, handling both IPv4 and IPv6 addresses. The function should also validate that the IPv6 address is in the recommended compressed format, where leading zeroes in each block can be omitted. Return True if the string is a valid IP address, False otherwise.
"""

import ipaddress

def is_valid_ip_address(ip):
    """
    Checks if a given string is a valid IP address, handling both IPv4 and IPv6 addresses.
    Also validates that the IPv6 address is in the recommended compressed format, 
    where leading zeroes in each block can be omitted.

    Args:
    ip (str): The IP address to be validated.

    Returns:
    bool: True if the string is a valid IP address, False otherwise.
    """
    try:
        ipaddress.ip_address(ip)
        if ':' in ip:
            return ipaddress.IPv6Address(ip).compressed == ip
        return True
    except ValueError:
        return False