"""
QUESTION:
Create a function called `extract_foremost_digit` that takes an alphanumeric string as input and returns the first digit encountered in the string. If no digit is found, the function should return `None`. The function should use regular expressions to locate and extract the digit.
"""

import re

def extract_foremost_digit(string):
    match = re.search(r'\d', string)
    if match:
        return match.group()
    else:
        return None