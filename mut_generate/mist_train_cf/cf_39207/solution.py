"""
QUESTION:
Write a function `extract_color_codes(code_snippet)` that takes a string `code_snippet` containing escape sequences and color codes as input, and returns a list of color codes in the order they appear. The color codes are represented as hexadecimal values preceded by `#`.
"""

import re

def entance(code_snippet):
    color_codes = re.findall(r'#\w+', code_snippet)
    return color_codes