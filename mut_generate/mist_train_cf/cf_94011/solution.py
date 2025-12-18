"""
QUESTION:
Write a function `capitalize_and_remove_special_chars` that takes a list of strings as input, removes any strings containing special characters (non-alphanumeric and non-whitespace), and returns a list of the remaining strings in uppercase.
"""

import re

def capitalize_and_remove_special_chars(strings):
    result = []
    for string in strings:
        # Check if string contains special characters
        if re.search(r'[^a-zA-Z0-9\s]', string) is None:
            # Capitalize the string and add to the result list
            result.append(string.upper())
    return result