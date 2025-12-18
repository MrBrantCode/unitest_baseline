"""
QUESTION:
Write a function `reverse_string(string)` that takes a string as input, removes all whitespace characters and non-alphabetic characters (including punctuation marks and special characters), and returns the remaining characters in reverse order. The function should handle both uppercase and lowercase characters.
"""

import re

def reverse_string(string):
    # Remove whitespace characters
    string = re.sub(r'\s', '', string)

    # Remove punctuation marks and special characters
    string = re.sub(r'[^A-Za-z]', '', string)

    # Reverse the string in place
    string = string[::-1]

    return string