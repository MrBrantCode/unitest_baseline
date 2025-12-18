"""
QUESTION:
Create a function named `extract_ipv6_addresses` that takes a string as input and returns a list of IPv6 addresses found in the string. The function should use regular expressions to match IPv6 addresses, which are represented as eight groups of four hexadecimal digits, each group separated by a colon (:). The function should not validate if the extracted addresses are valid IPv6 addresses.
"""

import re

def extract_ipv6_addresses(text):
    regex_pattern = r"((?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4})"
    ipv6_addresses = re.findall(regex_pattern, text)
    return ipv6_addresses