"""
QUESTION:
Create a function named `valid_hex_color` that checks if a given string is a valid hexadecimal color code. The function should validate both 6-digit RGB color codes (`#RRGGBB`) and 8-digit ARGB color codes (`#AARRGGBB`).
"""

import re

def valid_hex_color(s):
    pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{8})$'
    if re.match(pattern, s):
        return True
    return False