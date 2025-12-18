"""
QUESTION:
Create a function `get_matching_words(text)` that takes a string `text` as input and returns a list of words. The words should have the letters 'x' and 'y' appearing consecutively in them (in any order), be at least 10 characters long, and contain at least 1 digit.
"""

import re

def get_matching_words(text):
    pattern = re.compile(r'\b(\w*\d\w*[xy]{2}\w*|\w*[xy]{2}\w*\d\w*)\b')
    return [word for word in text.split() if pattern.fullmatch(word) and len(word) >= 10]