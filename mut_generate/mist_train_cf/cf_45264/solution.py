"""
QUESTION:
Write a function named `find_pattern` that takes a string `text` as input and returns a list of words that end with the suffix "able". The function should match whole words only and consider alphanumeric characters and underscores as valid word characters.
"""

import re

def find_pattern(text):
    pattern = r'\b\w+able\b'
    matches = re.findall(pattern, text)
    return matches