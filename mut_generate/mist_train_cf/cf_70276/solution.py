"""
QUESTION:
Create a function `is_ipv6(ipv6)` that takes a string `ipv6` as input and returns `True` if it represents a legitimate IPv6 network address and `False` otherwise. The IPv6 address is a 128-bit number, expressed as eight groups of four hexadecimal digits, divided by colons. The function should not support addresses with embedded IPv4 addresses or less-than-maximum length (short form) addresses.
"""

import re

def is_ipv6(ipv6):
    pattern = re.compile(""" 
    ^
    (?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}
    $
    """, re.VERBOSE)
    match = pattern.match(ipv6)
    return True if match else False