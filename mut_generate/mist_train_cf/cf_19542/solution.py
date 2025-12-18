"""
QUESTION:
Implement a function `string_formatter` that takes an input string, removes punctuation marks, converts to lowercase, splits into a list of words, removes duplicates, and returns the list of unique words in alphabetical order. The function should consider words with different capitalizations as the same word. The time complexity of the solution should be O(n log n) or better.
"""

import re

def string_formatter(input_string):
    input_string = re.sub(r'[^\w\s]', '', input_string.lower())
    words = input_string.split()
    unique_words = sorted(set(words))
    return unique_words