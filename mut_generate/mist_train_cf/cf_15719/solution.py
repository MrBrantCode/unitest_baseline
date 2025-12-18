"""
QUESTION:
Create a function `validate_string(input_string, length)` that checks if a given string has a specific length, contains only lowercase alphabets, and includes at least one digit and one special character.
"""

import re

def validate_string(input_string, length):
    if len(input_string) != length:
        return False
    if not input_string.islower():
        return False
    if not re.search(r'\d', input_string) or not re.search(r'[^a-zA-Z0-9]', input_string):
        return False
    return True