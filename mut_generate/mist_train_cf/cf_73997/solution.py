"""
QUESTION:
Create a function `is_hex_color(code)` that takes a string `code` as input and returns a boolean indicating whether the string is a valid hexadecimal color code. The code should be in the format `#XXXXXX` or `#XXX`, where `X` can be a hexadecimal character (0-F, both lowercase and uppercase). The function should return `True` if the string matches this pattern and `False` otherwise.
"""

import re

def is_hex_color(code):
    pattern = re.compile("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")
    if re.fullmatch(pattern, code):
        return True
    else:
        return False