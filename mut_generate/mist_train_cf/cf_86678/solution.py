"""
QUESTION:
Create a function named `filter_strings` that takes a list of strings and an integer `n` as input, and returns a new list of strings that meet the following conditions:

- The string contains both uppercase and lowercase letters.
- The string has a length of at least `n` characters.
- The string does not contain any special characters.

Note: Special characters include any characters that are not letters, such as digits and punctuation.
"""

import re

def filter_strings(strings, n):
    return [string for string in strings if len(string) >= n and re.match("^[a-zA-Z]+$", string) and any(char.isupper() for char in string) and any(char.islower() for char in string)]