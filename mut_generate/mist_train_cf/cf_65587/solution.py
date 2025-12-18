"""
QUESTION:
Create a function `match_string(word)` that takes a string `word` as input and returns `True` if the string matches the following conditions, and `False` otherwise. The string should start with a capital 'R' and end with either 'un', 'une', or 'unner'. The function should also validate that the string boundaries match the specified pattern exactly, excluding any strings that contain the prefix 'R' followed by any other characters.
"""

import re

def match_string(word):
    pattern = r'^R(?:un|une|unner)$'
    if re.match(pattern, word):
        return True
    return False