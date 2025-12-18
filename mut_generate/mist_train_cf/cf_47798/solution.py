"""
QUESTION:
Write a function `is_valid_mac_address(mac)` that takes a string `mac` as input and returns `True` if it is a valid MAC address, and `False` otherwise. A valid MAC address consists of 6 pairs of two-digit hexadecimal numbers separated by either a colon `:` or a hyphen `-`. The function should match the address format exactly from start to end, without allowing any additional characters.
"""

import re

def is_valid_mac_address(mac):
    pattern = "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
    if re.match(pattern, mac):
        return True
    else:
        return False