"""
QUESTION:
Write a function `validate_hex_color(color)` that validates a hexadecimal color code. The function should accept both full and shorthand versions of hexadecimal color codes (e.g. #FFFFFF and #FFF), and be case insensitive. The input is a string representing the hexadecimal color code. The function should return a boolean value indicating whether the input is a valid hexadecimal color code.
"""

import re

def validate_hex_color(color):
    pattern = re.compile(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?$')
    return bool(pattern.fullmatch(color))