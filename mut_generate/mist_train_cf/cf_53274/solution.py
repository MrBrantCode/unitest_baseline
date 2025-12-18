"""
QUESTION:
Write a function named `validate_string` that takes a string `construct` as input and returns `True` if the string starts with a non-alphanumeric character, followed by exactly 3 lowercase alphabetical characters, and ends with a number of 2 to 4 digits. Otherwise, return `False`.
"""

import re

def validate_string(construct):
    pattern = r'^[^a-zA-Z0-9][a-z]{3}\d{2,4}$'
    
    return bool(re.fullmatch(pattern, construct))