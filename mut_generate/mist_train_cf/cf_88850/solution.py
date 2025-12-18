"""
QUESTION:
Write a function `validate_ip_address(ip_address)` that takes a string as input and returns "IPv4" if the string is a valid IPv4 address, "IPv6" if the string is a valid IPv6 address in the recommended compressed format, and "Invalid IP address" otherwise. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

import re

def validate_ip_address(ip_address):
    # Regular expression pattern for IPv4 address
    ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

    # Regular expression pattern for IPv6 address in recommended compressed format
    ipv6_pattern = r'^(([0-9a-fA-F]{1,4}):){7}[0-9a-fA-F]{1,4}$'

    # Check if the given IP address matches either IPv4 or IPv6 pattern
    if re.match(ipv4_pattern, ip_address):
        return "IPv4"
    elif re.match(ipv6_pattern, ip_address):
        return "IPv6"
    else:
        return "Invalid IP address"