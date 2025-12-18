"""
QUESTION:
Create a function `validate_string(input_string)` that checks if the input string contains only letters (both uppercase and lowercase) and returns False if it contains any numbers, special characters, or whitespace characters, and True otherwise. The function should use regular expressions to match the pattern.
"""

import re

def validate_string(input_string):
    pattern = r'^[A-Za-z]+$'
    return bool(re.match(pattern, input_string))