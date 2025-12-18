"""
QUESTION:
Write a function named `remove_punctuation` that takes a text string as input and returns a new string where all punctuation marks, numbers, and special characters have been removed, leaving only letters and whitespace.
"""

import re

def remove_punctuation(text):
    clean_text = re.sub(r'[^\w\s]', '', text)
    return clean_text