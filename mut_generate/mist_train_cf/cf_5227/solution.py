"""
QUESTION:
Write a function `validate_ip_address(ip_address)` that takes a string `ip_address` as input and returns "IPv4" if it's a valid IPv4 address, "IPv6" if it's a valid IPv6 address in the recommended compressed format, and "Invalid IP address" otherwise. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

import re

def validate_ip_address(ip_address):
    ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    ipv6_pattern = r'^(([0-9a-fA-F]{1,4}):){7}[0-9a-fA-F]{1,4}$'

    if re.match(ipv4_pattern, ip_address):
        return "IPv4"
    elif re.match(ipv6_pattern, ip_address):
        return "IPv6"
    else:
        return "Invalid IP address"