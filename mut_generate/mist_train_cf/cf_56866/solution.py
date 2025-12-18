"""
QUESTION:
Create a function named `is_mac_address` that takes a string as input and returns a boolean indicating whether the string is a valid Media Access Control (MAC) address. A valid MAC address consists of six groups of two hexadecimal numbers, separated by either a colon (:) or a hyphen (-). The function should be case-insensitive and return False for any string that does not match this format.
"""

import re

def is_mac_address(mac):
    mac_pattern = re.compile('^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
    return bool(mac_pattern.match(mac))