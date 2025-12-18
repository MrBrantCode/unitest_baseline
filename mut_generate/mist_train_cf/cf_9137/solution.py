"""
QUESTION:
Create a function `is_scientific_notation` that takes a string as input and returns a boolean value indicating whether the string contains only numeric values in scientific notation with an exponent. The function should match strings that contain an optional sign (+ or -) at the start, followed by an integer or decimal number, and an optional exponent in scientific notation starting with 'e' or 'E', followed by an optional sign (+ or -), and one or more digits.
"""

import re

def is_scientific_notation(string):
    pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
    return bool(re.match(pattern, string))