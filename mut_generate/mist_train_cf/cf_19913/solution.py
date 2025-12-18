"""
QUESTION:
Write a function named `is_valid_ip_address` that takes a string as input and returns `True` if it is a valid IP address, either IPv4 or IPv6, and `False` otherwise. The function should also validate IPv6 addresses in the recommended compressed format, where leading zeroes in each block can be omitted.
"""

import ipaddress

def is_valid_ip_address(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False