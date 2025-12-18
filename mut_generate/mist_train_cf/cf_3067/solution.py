"""
QUESTION:
Write a function named `remove_punctuation` that takes a string as input and returns a new string with all punctuation marks, numbers, and special characters removed. The function should preserve spaces and alphabetic characters.
"""

import re

def remove_punctuation(text):
    # Remove punctuation marks, numbers, and special characters
    clean_text = re.sub(r'[^\w\s]', '', text)
    return clean_text