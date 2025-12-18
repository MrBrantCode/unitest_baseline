"""
QUESTION:
Create a function named `is_private_ip` that determines whether a given IP address is a valid private IP address. The function should accept a string representing the IP address and return True if the IP address is private and False otherwise. A valid private IP address should fall within the following ranges: 10.0.0.0 - 10.255.255.255, 172.16.0.0 - 172.31.255.255, or 192.168.0.0 - 192.168.255.255.
"""

import re

def is_private_ip(ip):
    """
    Determines whether a given IP address is a valid private IP address.

    Args:
    ip (str): The IP address to check.

    Returns:
    bool: True if the IP address is private, False otherwise.
    """
    pattern = r'^((10\.\d{1,3}\.\d{1,3}\.\d{1,3})|(172\.(1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3})|(192\.168\.\d{1,3}\.\d{1,3}))$'
    return bool(re.match(pattern, ip))