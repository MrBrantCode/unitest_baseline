"""
QUESTION:
Write a function named `parse_string` that takes a string as input, extracts unique words from the string, and returns them as a set. The function should handle strings containing punctuation marks, special characters, and words separated by hyphens, apostrophes, or other non-alphanumeric characters. The function should also perform case-insensitive comparison of words.
"""

import re

def parse_string(string):
    # Use regular expression to extract words from the string
    words = re.findall(r'\w+', string.lower())
    # Create a set to store unique words
    unique_words = set(words)
    return unique_words