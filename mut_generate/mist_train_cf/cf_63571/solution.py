"""
QUESTION:
Create a function named `find_pattern` that takes an input string. The function should identify and return the indices of all occurrences where 'x' (ignoring case sensitivity) is immediately followed by at least three 'w's (also ignoring case sensitivity) in the input string. If no such pattern exists, return "The pattern does not exist in the string." The function should disregard special characters, numbers, and any other irrelevant characters in the string.
"""

import re

def find_pattern(input_string):
    pattern = '[xX][wW]{3,}'
    matches = [match.start() for match in re.finditer(pattern, input_string)]
    
    if not matches:
        return "The pattern does not exist in the string."
    
    return matches