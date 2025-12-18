"""
QUESTION:
# Task
 A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

 The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

# Example

 For `inputString = "00-1B-63-84-45-E6"`, the output should be `true`;
 
 For `inputString = "Z1-1B-63-84-45-E6"`, the output should be `false`;
 
 For `inputString = "not a MAC-48 address"`, the output should be `false`.
 
# Input/Output

 - `[input]` string `inputString`
 
 - `[output]` a boolean value

    `true` if inputString corresponds to MAC-48 address naming rules, `false` otherwise.
"""

import re

def is_mac_48_address(inputString):
    """
    Validates whether the given input string is a valid MAC-48 address.

    Parameters:
    inputString (str): The input string to be validated.

    Returns:
    bool: True if the input string is a valid MAC-48 address, False otherwise.
    """
    return bool(re.match(r'^([0-9A-F]{2}[-]){5}([0-9A-F]{2})$', inputString.upper()))