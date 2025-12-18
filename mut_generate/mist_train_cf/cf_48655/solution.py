"""
QUESTION:
Construct a regular expression pattern that can extract IPv6 addresses from a given data set. The IPv6 addresses may be embedded in a mixed character data set including text, numbers, and special characters. The pattern should match standard IPv6 address format with 8 groups of 1-4 hexadecimal characters separated by colons, but does not need to match compressed IPv6 addresses.
"""

import re

def extract_ipv6(data):
    pattern = re.compile(r'(?:(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4})')
    return pattern.findall(data)