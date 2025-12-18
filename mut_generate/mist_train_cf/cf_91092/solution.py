"""
QUESTION:
Create a function `valid_string_lengths` that takes an array of strings and returns an array of their lengths. Each string in the array should be at least 5 characters long, no more than 15 characters long, and only contain letters. Return an empty array if no valid strings are found.
"""

import re

def valid_string_lengths(arr):
    valid_lengths = []
    for string in arr:
        if 5 <= len(string) <= 15 and not re.search(r'[0-9!@#$%^&*(),.?":{}|<>]', string):
            valid_lengths.append(len(string))
    return valid_lengths