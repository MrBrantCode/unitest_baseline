"""
QUESTION:
Write a function `match_string(s)` that takes a string `s` as input and returns `True` if the string has an 'a' followed by any number of characters, ending in 'b', and an error message otherwise. The function should handle non-string inputs and edge cases where the input string does not contain 'a' or 'b'.
"""

import re

def match_string(s):
    if not isinstance(s, str):
        return "Error: Input is not a string."
    pattern = 'a.*b$'
    if re.search(pattern, s):
        return True
    else:
        return "Error: The string does not contain 'a' followed by any characters, ending in 'b'."