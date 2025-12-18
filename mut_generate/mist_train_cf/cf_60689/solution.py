"""
QUESTION:
Write a function `ip_type(addr)` to validate and differentiate IPv6 addresses. The function should identify the address type as 'General IPv6', 'Link-local', 'Multicast', 'Loopback', or 'Unspecified'. If the address does not match any of these types, return 'Invalid'. The function should handle various formats of IPv6 addresses, including shortened forms (e.g., '::1' instead of '0000:0000:0000:0000:0000:0000:0000:0001').
"""

import re

# General IPv6 address
ipv6_pattern = re.compile(r'^([0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}$')

# Link-local address
link_local_pattern = re.compile(r'^fe80:([0-9a-fA-F]{0,4}:){0,5}[0-9a-fA-F]{0,4}$')

# Multicast address
multicast_pattern = re.compile(r'^ff[0-9a-fA-F]{2}:([0-9a-fA-F]{0,4}:){0,6}[0-9a-fA-F]{0,4}$')

# Loopback address
loopback_pattern = re.compile(r'^::1$')

# Unspecified address
unspecified_pattern = re.compile(r'^::$')

def ip_type(addr):
    if link_local_pattern.match(addr):
        return "Link-local"
    elif multicast_pattern.match(addr):
        return "Multicast"
    elif loopback_pattern.match(addr):
        return "Loopback"
    elif unspecified_pattern.match(addr):
        return "Unspecified"
    elif ipv6_pattern.match(addr):
        return "General IPv6"
    else:
        return "Invalid"