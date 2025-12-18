"""
QUESTION:
Create a function `is_valid_ipv6` that takes a string `address` as input and returns a boolean indicating whether the string is a valid IPv6 address according to standard IP address specifications, following these rules: 
- The string should consist of 8 groups of hexadecimal digits separated by colons.
- Each group should contain between 0 and 4 hexadecimal digits.
- The string should not be in compressed or shortened format.
"""

import re

def is_valid_ipv6(address):
    pattern = re.compile(r'^([0-9a-fA-F]{0,4}:){7}([0-9a-fA-F]{1,4})$')
    return bool(pattern.match(address))