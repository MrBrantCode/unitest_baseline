"""
QUESTION:
Write a function `is_valid_number` that determines whether a given string contains a valid number. The string should start with a letter, end with a digit, and have at least two special characters in between. The valid number should be at least 8 characters long and consist only of digits and alphabetic characters.
"""

import re

def is_valid_number(string):
    pattern = r"^[a-zA-Z][!@#$%^&*()-=_+~`<>?/.,:;\[\]{}|]{2,}[0-9]$"
    return bool(re.match(pattern, string))