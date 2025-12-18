"""
QUESTION:
Write a function `find_palindromes(sentence)` that takes a string `sentence` as input, identifies all the words in the sentence, and returns a list of the words that are palindromes.
"""

import re

def find_palindromes(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    palindromes = [word for word in words if word == word[::-1]]
    return palindromes