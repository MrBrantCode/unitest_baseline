"""
QUESTION:
Write a function `isValidMACAddress(mac)` that takes a string `mac` as input and returns `True` if it matches the valid Ethernet MAC address format and `False` otherwise. A valid Ethernet MAC address consists of six groups of two hexadecimal digits, separated by colons.
"""

import re

def isValidMACAddress(mac):
    mac_addr_pattern = r'\A([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}\Z'
    return bool(re.match(mac_addr_pattern, mac))