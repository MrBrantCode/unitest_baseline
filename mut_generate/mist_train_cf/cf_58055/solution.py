"""
QUESTION:
Write a function `is_valid_hex_code(hex_code)` that determines if a given string is a valid hexadecimal color code, which must start with a `#` and be followed by either 3 or 6 hexadecimal characters (`A-F`, `a-f`, or `0-9`). The function should return `True` if the string is a valid hexadecimal color code and `False` otherwise.
"""

import re

def is_valid_hex_code(hex_code):
    pattern = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
    return bool(re.search(pattern, hex_code))