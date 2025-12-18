"""
QUESTION:
Create a function `parse_string` that takes a string as input and returns a set of unique words. The function should be able to handle strings containing punctuation marks, special characters, and words separated by hyphens, apostrophes, or other non-alphanumeric characters. The comparison of words should be case-insensitive.
"""

import re

def parse_string(string):
    # Use regular expression to extract words from the string
    words = re.findall(r'\w+', string.lower())
    # Create a set to store unique words
    unique_words = set(words)
    return unique_words