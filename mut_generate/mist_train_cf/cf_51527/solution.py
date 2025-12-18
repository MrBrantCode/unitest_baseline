"""
QUESTION:
Write a function `find_words` that takes a string as input and returns all words that contain the alphabets 'x' and 'y' in sequential succession. The function should be case-sensitive and consider word boundaries.
"""

import re

def find_words(string):
    pattern = re.compile(r'\b\w*x\w*y\w*\b')
    matches = pattern.findall(string)
    return matches