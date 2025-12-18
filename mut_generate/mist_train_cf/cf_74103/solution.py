"""
QUESTION:
Design a function `has_dual_vowels(word)` that takes a string `word` as input and returns `True` if the word contains dual vowel clusters (i.e., two vowels together), and `False` otherwise. Additionally, create a function `magnify(word)` that takes a string `word` as input and returns the word in uppercase.
"""

import re

def has_dual_vowels(word):
    return re.search(r'[aeiou]{2}', word) is not None

def magnify(word):
    return word.upper()