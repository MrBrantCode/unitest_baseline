"""
QUESTION:
Construct a function named `is_valid_ipv6_address` that checks if a given string is a valid IPv6 address, ignoring any leading or trailing whitespace characters. The function should return True for loopback addresses starting with "::1" and link-local addresses starting with "fe80:", and False otherwise.
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
    ipv6_pattern = r'^(([0-9A-Fa-f]{1,4}:){7}|([0-9A-Fa-f]{1,4}:){1,7}:|([0-9A-Fa-f]{1,4}:){1,6}(:[0-9A-Fa-f]{1,4}){1,2}|([0-9A-Fa-f]{1,4}:){1,5}(:[0-9A-Fa-f]{1,4}){1,3}|([0-9A-Fa-f]{1,4}:){1,4}(:[0-9A-Fa-f]{1,4}){1,4}|([0-9A-Fa-f]{1,4}:){1,3}(:[0-9A-Fa-f]{1,4}){1,5}|([0-9A-Fa-f]{1,4}:){1,2}(:[0-9A-Fa-f]{1,4}){1,6}|([0-9A-Fa-f]{1,4}:){1}(:[0-9A-Fa-f]{1,4}){1,7}|([0-9A-Fa-f]{1,4}){1,8})$'
    if re.match(ipv6_pattern, address, re.IGNORECASE):
        return True

    return False