"""
QUESTION:
Implement the function `parse_string(string)` that takes a string as input and returns a list of words. The function should be case-insensitive, removing any punctuation marks and non-alphabetic characters from the string before parsing, and handle multiple spaces between words. If the input string is empty or consists only of punctuation marks, the function should return an empty list.
"""

import re

def parse_string(string):
    # Remove punctuation marks
    string = re.sub(r'[^\w\s]', '', string)

    # Convert string to lowercase and split into words
    words = string.lower().split()

    return words