"""
QUESTION:
Write a function `is_hex_color_code` to determine if a given string is a valid hex color code. A valid hex color code is a string that starts with a '#' followed by either 3 or 6 hexadecimal digits (0-9, A-F, or a-f).
"""

def is_hex_color_code(s):
    return bool(s.startswith('#') and len(s) in (4, 7) and all(c in '0123456789ABCDEFabcdef' for c in s[1:]))