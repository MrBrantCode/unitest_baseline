"""
QUESTION:
Write a function `get_max_length_strings(strings)` that takes a list of strings as input and returns a list of strings with the maximum length. The function should only consider strings that contain only alphabets and spaces, and the maximum length of any individual string should not exceed 50 characters. If there are multiple strings with the same maximum length, the function should return all of them in alphabetical order. If the input list is empty, the function should return an empty list.
"""

import re

def get_max_length_strings(strings):
    max_length = 0
    valid_strings = []

    # Find the maximum length of valid strings
    for string in strings:
        if bool(re.match('^[a-zA-Z\s]+$', string)) and len(string) <= 50:
            max_length = max(max_length, len(string))

    # Get all the valid strings with maximum length
    for string in strings:
        if bool(re.match('^[a-zA-Z\s]+$', string)) and len(string) <= 50 and len(string) == max_length:
            valid_strings.append(string)

    return sorted(valid_strings)