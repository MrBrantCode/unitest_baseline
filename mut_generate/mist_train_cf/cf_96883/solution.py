"""
QUESTION:
Define a function named `is_valid_ipv6_address` that takes a string as input and returns True if it is a valid IPv6 address and False otherwise. The function should follow these rules:
- The input string should not start or end with a colon.
- The input string should not contain consecutive colons (::) more than once or have them in the middle if it does.
- The input string should contain at most 8 groups of hexadecimal digits separated by colons.
- Each group should be a hexadecimal number within the range of 0000 to FFFF and not contain leading zeros (unless it is 0000).
- The input string should not contain any non-hexadecimal characters other than colons.
"""

import re

def is_valid_ipv6_address(ip_str):
    # Check if the address starts or ends with a colon
    if ip_str.startswith(':') or ip_str.endswith(':'):
        return False

    # Split the address into groups using colons as separators
    groups = ip_str.split(':')

    # Check if the number of groups is valid
    if len(groups) > 8:
        return False

    # Check for consecutive colons (::) in the middle of the address
    if '::' in ip_str:
        if ip_str.count('::') > 1:
            return False
        elif ip_str.index('::') != ip_str.rindex('::'):
            return False

    # Check if each group is a valid hexadecimal number
    for group in groups:
        # Check if the group contains non-hexadecimal characters
        if not re.match(r'^[0-9A-Fa-f]{1,4}$', group):
            return False

        # Check if the group contains leading zeros
        if group.startswith('0') and len(group) > 1:
            return False

    return True