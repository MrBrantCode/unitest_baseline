"""
QUESTION:
Create a function `check_string` that takes a string as input and returns `True` if it meets the following conditions, otherwise return `False`. The string must contain only alphabetical characters and have a length of at least 10 characters. Additionally, the string must contain at least two uppercase letters, two lowercase letters. However, the current solution includes checking for two digits, but this is logically contradictory with checking if a string contains only alphabetical characters. Therefore, we should exclude the condition of checking for digits.
"""

import re

def entrance(string):
    # Check if the string contains only alphabetical characters and has a length of at least 10 characters
    if not string.isalpha() or len(string) < 10:
        return False

    # Check if the string contains at least two uppercase letters, two lowercase letters
    uppercase_count = len(re.findall(r'[A-Z]', string))
    lowercase_count = len(re.findall(r'[a-z]', string))

    if uppercase_count < 2 or lowercase_count < 2:
        return False

    return True