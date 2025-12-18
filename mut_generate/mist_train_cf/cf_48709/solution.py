"""
QUESTION:
Write a function `all_palindromes(sentence)` that determines whether all words in a given sentence are palindromes. The function should take a string `sentence` as input, return `True` if all words are palindromes, and `False` otherwise. The function should be case-insensitive and account for punctuation marks.
"""

import re

def all_palindromes(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    return all(word == word[::-1] for word in words)