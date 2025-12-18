"""
QUESTION:
Write a function `sort_string(string)` that takes a string of words as input, removes any duplicate words, ignores words containing numbers or special characters, and returns the remaining words sorted alphabetically in descending order based on their length.
"""

import re

def sort_string(string):
    words = string.split()
    words = list(set(words))
    words = [word for word in words if re.match(r'^[a-zA-Z]+$', word)]
    words.sort(key=len, reverse=True)
    return ' '.join(words)