"""
QUESTION:
Write a function `validate_and_format_mac(mac: str) -> str` that takes a string `mac` representing a MAC address as input and returns a formatted MAC address if it is valid. A valid MAC address should consist of 12 hexadecimal digits (0-9, a-f, A-F) without any delimiters other than colons and be exactly 17 characters long, including the colons. The function should return "Invalid MAC address" if the input MAC address is not valid.
"""

import re

def validate_and_format_mac(mac: str) -> str:
    # Remove any delimiters from the input MAC address
    mac = mac.replace(":", "").replace("-", "")

    # Check if the MAC address is valid
    if re.match(r'^([0-9a-fA-F]{2}){6}$', mac):
        # Format the valid MAC address with colons
        formatted_mac = ":".join([mac[i : i + 2] for i in range(0, 12, 2)])
        return formatted_mac
    else:
        return "Invalid MAC address"