"""
QUESTION:
Write a function `find_ip_addresses` that verifies whether a given string includes valid IPv4 or IPv6 addresses and indicates which format each address is in. The function should return a tuple containing two lists: the first list contains the IPv4 addresses found in the string, and the second list contains the IPv6 addresses found in the string. The function should correctly handle strings that contain both IPv4 and IPv6 addresses.
"""

import re

def find_ip_addresses(s):
    # IPv4 regular expression pattern
    ipv4_pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'

    # IPv6 regular expression pattern
    ipv6_pattern = r'\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b'

    ipv4_addresses = re.findall(ipv4_pattern, s)
    ipv6_addresses = re.findall(ipv6_pattern, s)

    return ipv4_addresses, ipv6_addresses