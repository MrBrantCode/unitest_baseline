"""
QUESTION:
Write a function named `is_scientific_notation` that checks whether a given string contains only numeric values in scientific notation with an exponent. The function should return `True` if the string is in scientific notation and `False` otherwise. The function should handle both 'e' and 'E' for the exponent part and optional signs (+ or -) before the number and the exponent.
"""

import re

def is_scientific_notation(string):
    pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
    return bool(re.match(pattern, string))