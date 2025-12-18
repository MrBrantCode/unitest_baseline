"""
QUESTION:
Create a function called `valid_string_lengths` that takes an array of strings as input. The function should return an array of the lengths of the strings in the input array, but only if each string is at least 5 characters long and no more than 15 characters long, and does not contain numbers or special characters. If no valid strings are found, the function should return an empty array.
"""

import re

def valid_string_lengths(arr):
    valid_lengths = []
    for string in arr:
        if 5 <= len(string) <= 15 and not re.search(r'[0-9!@#$%^&*(),.?":{}|<>]', string):
            valid_lengths.append(len(string))
    return valid_lengths