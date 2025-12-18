"""
QUESTION:
Create a function `extractAddressAndPort(CLUSTER_ADDR)` that takes a string `CLUSTER_ADDR` as input, representing an IP address and a port number, and returns a tuple `(CLUSTER_IP, CLUSTER_PORT)` containing the extracted IP address and port number. The `CLUSTER_ADDR` can be in one of two formats: IPv6 enclosed in square brackets or IPv4 in standard dotted-decimal notation, both followed by a port number. The port number is a positive integer.
"""

import re

def extractAddressAndPort(CLUSTER_ADDR):
    ipv6_pattern = r'\[([0-9a-fA-F:]+)\]:(\d+)'
    ipv4_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)'

    ipv6_match = re.match(ipv6_pattern, CLUSTER_ADDR)
    ipv4_match = re.match(ipv4_pattern, CLUSTER_ADDR)

    if ipv6_match:
        return ipv6_match.group(1), int(ipv6_match.group(2))
    elif ipv4_match:
        return ipv4_match.group(1), int(ipv4_match.group(2))
    else:
        return None  # Handle invalid input format