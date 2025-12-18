"""
QUESTION:
Create a function `find_even_numbers` that takes a string as input and returns a list of numeric segments that represent even numbers. The function should use regular expressions to identify even numbers, which are defined as numbers that end with the digits 0, 2, 4, 6, or 8.
"""

import re

def find_even_numbers(string):
    pattern = r'\b[0-9]*[02468]\b'
    return re.findall(pattern, string)