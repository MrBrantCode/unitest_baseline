"""
QUESTION:
Create a function called `match_float` that takes a string as input and returns True if the string matches a float number with at least one decimal place, otherwise returns False. The function should match both positive and negative numbers, and the decimal part is optional but must have at least one digit if present.
"""

import re

def match_float(s):
    pattern = re.compile(r'^-?\d+(\.\d+)?$')
    return bool(pattern.match(s))