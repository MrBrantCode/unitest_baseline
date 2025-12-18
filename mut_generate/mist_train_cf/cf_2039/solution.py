"""
QUESTION:
Write a function `is_valid_hexadecimal(string)` that checks if a given string represents a valid hexadecimal number. The string should start with '0x', contain only digits 0-9 and letters A-F, have a maximum length of 8 characters, and no leading zeros before the '0x' prefix.
"""

import re

def is_valid_hexadecimal(string):
    pattern = r'^0x[A-Fa-f0-9]{1,6}$'
    return bool(re.match(pattern, string))