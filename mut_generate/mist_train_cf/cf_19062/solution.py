"""
QUESTION:
Write a function `parse_string` that takes a string as input, removes all non-alphanumeric characters, converts the string to lowercase, and returns a list of words. The function should handle multiple spaces between words, empty strings, and strings containing only non-alphanumeric characters, returning an empty list in such cases.
"""

import re

def parse_string(string):
    # Remove punctuation marks
    string = re.sub(r'[^\w\s]', '', string)

    # Convert string to lowercase and split into words
    words = string.lower().split()

    return words