"""
QUESTION:
Write a function named `validateIP` that takes an IP address as input and returns `True` if it's a valid IPv4 or IPv6 address, and `False` otherwise. The function should check for valid IPv4 address segments (0-255) and valid IPv6 address segments (0-FFFF).
"""

import re

def validateIP(ip):
  if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip):
    return True
  elif re.match(r"^((?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4})$", ip):
    return True
  else:
    return False