"""
QUESTION:
Create a function called `odd_characters` that takes a string of characters as input. The function should return a new string containing only the alphabetic characters from the odd positions of the original string, maintaining their original order and ignoring non-alphabetic characters.
"""

import re

def odd_characters(input_string):
    pattern = re.compile('[A-Za-z]')
    return ''.join(re.findall(pattern, input_string)[1::2])