"""
QUESTION:
Design a function named `split_sentence` that takes a string `sentence` as input and returns a list of substrings. The function should split the input string into words and separate punctuation and special characters from the words. The function should handle punctuation and special characters as individual items in the output list.
"""

import re

def split_sentence(sentence):
    words = re.findall(r'\w+|[^\w\s]', sentence)
    return words