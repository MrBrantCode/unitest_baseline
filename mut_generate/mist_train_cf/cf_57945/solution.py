"""
QUESTION:
Write a function `find_phoenix(text)` that checks if the word "phoenix" (ignoring case) is at the beginning of the input string `text`. The function should return `True` if "phoenix" is found at the start of the string and `False` otherwise.
"""

import re

def find_phoenix(text):
    pattern = r"^[Pp][Hh][Oo][Ee][Nn][Ii][Xx]"
    match = re.match(pattern, text)
    if match:
        return True
    return False