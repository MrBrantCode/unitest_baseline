"""
QUESTION:
Construct a function `is_valid_ipv6_address(address)` that takes a string `address` as input and returns `True` if it's a valid IPv6 address, and `False` otherwise. The function should ignore leading and trailing whitespace characters in the input string. A valid IPv6 address should either be a loopback address starting with "::1", a link-local address starting with "fe80:", or a standard IPv6 address in the format of up to 8 groups of 1-4 hexadecimal digits separated by colons.
"""

import re

def is_valid_ipv6_address(address):
    # Remove leading and trailing whitespace characters
    address = address.strip()

    # Check if the address is a loopback address
    if address.startswith("::1"):
        return True

    # Check if the address is a link-local address
    if address.startswith("fe80:"):
        return True

    # Use regular expression to validate the address format
    ipv6_pattern = r'^(([0-9A-Fa-f]{1,4}):){7}([0-9A-Fa-f]{1,4})$'
    if re.match(ipv6_pattern, address):
        return True

    return False