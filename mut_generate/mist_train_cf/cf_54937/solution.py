"""
QUESTION:
Implement a Python function `is_valid_ipv6(ip)` to check if a given string `ip` is a valid IPv6 address. The function should return `True` if the string is a valid IPv6 address and `False` otherwise. The function should also be able to identify reserved IPv6 addresses like 'loopback' ('::1') and 'unspecified' ('::'). 

A valid IPv6 address is one that consists of eight groups of four hexadecimal digits, separated by colons (:). The function should check for the following conditions: 
- The string should have exactly eight groups separated by colons, unless it contains a double colon (::) which represents one or more groups of four zeros.
- Each group should contain only hexadecimal digits and not be more than 4 characters long.
- There should be at most one double colon (::) in the IP address, and it should not be surrounded by digits.

Additionally, implement a function `is_reserved_ipv6(ip)` to check if a given string `ip` is a reserved IPv6 address. The function should return `True` if the string is a reserved IPv6 address and `False` otherwise.
"""

import re

def is_valid_ipv6(ip):
    """Check if a given string is a valid IPv6 address."""
    fields = ip.split(":")
    if len(fields) > 8:
        return False
    if "::" in ip:
        if ip.count("::") > 1 or (ip.count(':') - 1 < 2):
            return False
        fields.remove('')
    for field in fields:
        if len(field) > 4:
            return False
        if not re.match('^[0-9a-fA-F]{1,4}$', field):
            return False
    return True

def is_reserved_ipv6(ip):
    """Check if a given string is a reserved IPv6 address."""
    reserved_ips = ["::1", "::"]
    return ip in reserved_ips