"""
QUESTION:
Create a function `match_hex(s)` that matches a string `s` containing a hexadecimal number followed by a lower-case vowel, where the hexadecimal number must not have any leading zeroes unless the number itself is zero, and the hexadecimal number falls within the range of a positive 32-bit integer.
"""

import re

def match_hex(s):
    pattern = r"^(0x)?([1-9a-fA-F][0-9a-fA-F]*|0)[aeiou]$"
    match = re.match(pattern, s)
    if match:
        hex_number = match.group(2)
        if int(hex_number, 16) <= 0xffffffff:
            return True
    return False