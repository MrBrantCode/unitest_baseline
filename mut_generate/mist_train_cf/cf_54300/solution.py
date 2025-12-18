"""
QUESTION:
Create a function named `is_valid_mac` that takes one parameter `mac` to validate if the given string is a valid MAC address. A valid MAC address consists of six groups of two hexadecimal digits separated by either colons (:) or dashes (-). The function should return `True` if the MAC address is valid and `False` otherwise.
"""

import re

def is_valid_mac(mac):
    pattern = re.compile(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$")
    return bool(pattern.match(mac))