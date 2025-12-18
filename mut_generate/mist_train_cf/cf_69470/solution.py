"""
QUESTION:
Write a function `validate_ipv6_address(addr)` to validate a given IPv6 address. The function should return `True` if the address is valid and `False` otherwise. The IPv6 address should be in the format of 8 groups of hexadecimal numbers separated by colons (:), with each group having 1 to 4 hex digits and allowing leading zeros.
"""

import re

def validate_ipv6_address(addr):
    pattern = re.compile(r'^([0-9a-fA-F]{0,4}:){7}[0-9a-fA-F]{0,4}$')
    return pattern.match(addr) is not None