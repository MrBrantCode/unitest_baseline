"""
QUESTION:
Create a function `is_valid_ipv6(ip)` that takes an IPv6 address as input and returns `True` if the address is valid and `False` otherwise. The function should be able to match most IPv6 addresses, including those in shortened form. The IPv6 address is a 128-bit address written in hexadecimal, divided into 8 blocks, and sometimes contains missing blocks represented by full colons.
"""

import re

def is_valid_ipv6(ip):
    pattern = re.compile(r'^([0-9a-fA-F]{0,4}:){2,7}([0-9a-fA-F]){0,4}$')
    return bool(pattern.match(ip))