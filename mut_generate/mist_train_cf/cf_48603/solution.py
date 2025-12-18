"""
QUESTION:
Write a function `valid_ipv6_address(ip)` that checks if a given string `ip` is a valid full-length IPv6 address. A valid full-length IPv6 address consists of eight groups of four hexadecimal digits, each group representing 16 bits, separated by colons (:). The function should return `True` if the input string is a valid full-length IPv6 address and `False` otherwise.
"""

import re

def valid_ipv6_address(ip):
    pattern = re.compile(r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$")
    return pattern.match(ip) is not None