"""
QUESTION:
Create a function named `get_even_characters` that takes a string of characters as input and returns a new string containing only the alphabetic characters at even positions in the original string, ignoring non-alphabetic characters and maintaining the original order. The function should use regular expressions.
"""

import re

def get_even_characters(string):
    regex = r'[a-zA-Z]'
    matches = re.findall(regex, string)
    result = "".join([matches[i] for i in range(len(matches)) if i % 2 == 0])
    return result