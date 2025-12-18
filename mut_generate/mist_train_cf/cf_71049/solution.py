"""
QUESTION:
Write a function called `classify_addresses` that takes a list of IP addresses as input and returns a dictionary containing two lists of tuples, one for valid IPv4 addresses and one for valid IPv6 addresses. Each tuple should contain the address and a rank value that represents its integer value for sorting purposes.

The function should use regular expressions to validate the addresses. A valid IPv4 address consists of four 1-byte numbers separated by periods (.), where each number is between 0 and 255. A valid IPv6 address consists of eight 2-byte hexadecimal numbers separated by colons (:).

The function should return a dictionary with the following structure: `{"IPv4": [(address, rank), ...], "IPv6": [(address, rank), ...]}`, where the lists are sorted by rank in ascending order.
"""

import re

def ip_address_rank(address):
    """
    Assigns a rank to an IP address based on its integer value.
    """
    if ":" in address:  # IPv6
        rank = int(address.replace(":", ""), 16)
    else:  # IPv4
        rank = sum(int(byte) << (8 * i) for i, byte in enumerate(address.split(".")[::-1]))
    return rank

def classify_addresses(addresses):
    """
    Classifies a list of IP addresses into IPv4 and IPv6, and assigns each a rank.
    """
    ipv4_pattern = re.compile(r"^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$")
    ipv6_pattern = re.compile(r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$")

    ipv4_addresses = []
    ipv6_addresses = []

    for address in addresses:
        if ipv4_pattern.match(address):
            ipv4_addresses.append((address, ip_address_rank(address)))
        elif ipv6_pattern.match(address):
            ipv6_addresses.append((address, ip_address_rank(address)))

    # sort the addresses by rank
    ipv4_addresses.sort(key=lambda x: x[1])
    ipv6_addresses.sort(key=lambda x: x[1])

    return {
        "IPv4": ipv4_addresses,
        "IPv6": ipv6_addresses
    }