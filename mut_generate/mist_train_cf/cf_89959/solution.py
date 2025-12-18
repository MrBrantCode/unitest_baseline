"""
QUESTION:
Create a function `check_string(string)` that takes a string as input. The function should return `True` if the string contains only alphabetical characters, has a length of at least 10 characters, contains at least two uppercase letters, two lowercase letters, and two digits, and `False` otherwise.
"""

import re

def check_string(string):
    # Check if the string contains only alphabetical characters and has a length of at least 10 characters
    if not string.isalpha() or len(string) < 10:
        return False

    # Check if the string contains at least two uppercase letters, two lowercase letters, and two digits
    uppercase_count = len(re.findall(r'[A-Z]', string))
    lowercase_count = len(re.findall(r'[a-z]', string))
    digit_count = len(re.findall(r'\d', string))

    if uppercase_count < 2 or lowercase_count < 2 or digit_count < 2:
        return False

    return True