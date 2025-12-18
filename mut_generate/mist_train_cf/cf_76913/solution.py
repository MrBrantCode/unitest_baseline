"""
QUESTION:
Design a function `is_valid_ipv6(ip)` that takes a string `ip` as input and returns a boolean indicating whether it is a valid IPv6 address. The function should follow the standard IPv6 network protocol rules. Note that the function should match the basic structure of an IPv6 address, but does not need to handle all special cases or invalid addresses.
"""

import re

def is_valid_ipv6(ip):
  pattern = re.compile('^([0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}$')
  return bool(pattern.match(ip))