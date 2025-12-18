"""
QUESTION:
Create a function `is_valid_ipv6(ip)` that takes an IPv6 address as a string `ip` and returns `True` if the address is valid according to the IPv6 address format rules and `False` otherwise. The function should handle various IPv6 address formats, including full, short, and with/without leading zeros, as well as special formats like link-local addresses with interface-id and IPv4-mapped/IPv4-compatible notation. The function should be case-insensitive.
"""

import re

def is_valid_ipv6(ip):
    pattern = re.compile(r'^'
                         r'('
                         r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|'
                         r'([0-9a-fA-F]{1,4}:){1,7}:|'
                         r'([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|'
                         r'([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|'
                         r'([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|'
                         r'([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|'
                         r'([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|'
                         r'[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|'
                         r':((:[0-9a-fA-F]{1,4}){1,7}|:)|'
                         r'fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|'
                         r'::(ffff(:0{1,4}){0,1}:){0,1}'
                         r'((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}'
                         r'(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|'
                         r'([0-9a-fA-F]{1,4}:){1,4}:'
                         r'((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}'
                         r'(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'
                         r')\Z',
                         re.VERBOSE | re.IGNORECASE | re.DOTALL)
    return bool(pattern.match(ip))