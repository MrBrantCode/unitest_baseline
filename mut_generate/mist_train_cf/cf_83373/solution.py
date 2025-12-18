"""
QUESTION:
Create a function named `validate_addresses` that takes a list of strings representing network addresses as input. The function should use regular expressions to validate and separate the addresses into two categories: MAC (Media Access Control) addresses and IPv6 addresses. 

A valid MAC address consists of six groups of two hexadecimal digits, separated by colons or hyphens, while a valid IPv6 address consists of eight groups of four hexadecimal digits, separated by colons. The function should return two lists: one for valid MAC addresses and one for valid IPv6 addresses.
"""

import re

def validate_addresses(addresses):
    valid_mac_addresses = []
    valid_ipv6_addresses = []
    
    pattern_MAC = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    pattern_IPv6 = r'^([0-9a-fA-F]{4}:){7}[0-9a-fA-F]{4}$'
    
    for address in addresses:
        if re.match(pattern_MAC, address):
            valid_mac_addresses.append(address)
        elif re.match(pattern_IPv6, address):
            valid_ipv6_addresses.append(address)
            
    return valid_mac_addresses, valid_ipv6_addresses