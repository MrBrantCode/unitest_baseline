"""
QUESTION:
Implement the `extract_ip` function, which takes a string `input_str` as its parameter and returns a tuple `(ipv4, ipv6)` containing the extracted IPv4 and IPv6 addresses. IPv4 addresses are represented in the standard dot-decimal notation, while IPv6 addresses are represented in the standard colon-hexadecimal notation. If no valid IPv4 or IPv6 addresses are found, the corresponding tuple element should be an empty string.
"""

import re

def extract_ip(input_str: str) -> (str, str):
    ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ipv6_pattern = r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b'

    ipv4_match = re.search(ipv4_pattern, input_str)
    ipv6_match = re.search(ipv6_pattern, input_str)

    ipv4 = ipv4_match.group(0) if ipv4_match else ''
    ipv6 = ipv6_match.group(0) if ipv6_match else ''

    return (ipv4, ipv6)