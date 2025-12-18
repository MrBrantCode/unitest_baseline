"""
QUESTION:
Write a function called `validate_address` that validates a given string of IP addresses. The function should validate both IPv4 and IPv6 addresses. IPv4 addresses consist of four bytes (0 to 255) separated by periods, and each byte should not have leading zeros unless it is zero itself. IPv6 addresses consist of eight groups of one to four hexadecimal digits separated by colons, with each group having at most four digits. The function should return `True` if the IP address is valid and `False` otherwise.
"""

import re

def validate_address(ip):
    ipv4_pattern = re.compile(
        r'^(?:(?:25[0-5]|2[0-4][0-9]|(?!0)[1-9][0-9]?|0)\.){3}(?:25[0-5]|2[0-4][0-9]|(?!0)[1-9][0-9]?|0)$'
    )
    ipv6_pattern = re.compile(
        r'^(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}$'
    )
    if ipv4_pattern.match(ip) or ipv6_pattern.match(ip):
        return True
    else:
        return False