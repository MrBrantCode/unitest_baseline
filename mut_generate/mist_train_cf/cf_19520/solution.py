"""
QUESTION:
Write a function called `reverse_words` that takes a sentence as input and returns a list of words in reverse order. The function should use regular expressions to split the sentence into words and should not use the built-in split function.
"""

import re

def reverse_words(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    return words[::-1]