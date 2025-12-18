"""
QUESTION:
Compose a function named `check_hex_color_code` that takes a string `code` as input and returns `True` if the string is a legal hexadecimal color code sequence and `False` otherwise. A legal hexadecimal color code sequence is a string that starts with '#' followed by either three or six hexadecimal digits (0-9, a-f, or A-F). The function should account for both shorthand (e.g., `#FFF`) and full (e.g., `#FFFFFF`) hexadecimal color codes.
"""

import re

def check_hex_color_code(code):
    hex_color_regex = r'^#(?:[0-9a-fA-F]{3}){1,2}$'
    if re.match(hex_color_regex, code):
        return True
    else:
        return False