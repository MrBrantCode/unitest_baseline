"""
QUESTION:
Create a function called `check_ip` that takes an input string and returns its IP address type. The function should identify whether the input string is an IPv4 or IPv6 address and return 'IPv4' or 'IPv6' accordingly. If the input string is not a valid IP address, the function should return 'Invalid format'.
"""

import ipaddress

def check_ip(input_string):
    try:
        ip = ipaddress.ip_address(input_string)
        if ip.version == 4:
            return 'IPv4'
        else:
            return 'IPv6'
    except ValueError:
        return 'Invalid format'