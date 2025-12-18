"""
QUESTION:
Create a function `capitalize_and_remove_special_chars` that takes a list of strings as input and returns a new list containing the capitalized version of strings that only include alphanumeric characters and whitespace, excluding any strings with special characters.
"""

import re

def capitalize_and_remove_special_chars(strings):
    result = []
    for string in strings:
        if re.search(r'[^a-zA-Z0-9\s]', string) is None:
            result.append(string.upper())
    return result