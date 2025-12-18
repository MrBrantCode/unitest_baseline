"""
QUESTION:
Create a function `is_valid_ipv4_address` that uses regular expression to determine whether a given string is a valid IPv4 address. The function should return `True` if the string is a valid IPv4 address and `False` otherwise.
"""

import re

def is_valid_ipv4_address(ip):
    """
    This function checks whether a given string is a valid IPv4 address.
    
    Args:
        ip (str): The IP address to be validated.
    
    Returns:
        bool: True if the string is a valid IPv4 address, False otherwise.
    """
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}$"
    return bool(re.match(pattern, ip))