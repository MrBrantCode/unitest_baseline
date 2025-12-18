"""
QUESTION:
Write a function `remove_non_alphanumeric` that takes a string as input, removes all non-alphanumeric characters, converts the remaining characters to lowercase, and returns the resulting string sorted in reverse alphabetical order. The function should not use any additional data structures or libraries beyond the Python standard library.
"""

import re

def remove_non_alphanumeric(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    sorted_text = ''.join(sorted(cleaned_text, reverse=True))
    return sorted_text