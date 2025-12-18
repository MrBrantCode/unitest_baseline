"""
QUESTION:
Create a function `remove_duplicates` that takes a string `sentence` as input, removes any duplicate words while maintaining the original order and case sensitivity, and returns the resulting string. The solution must have a time complexity better than O(n^2), where n is the number of words in the sentence.
"""

import re
from itertools import groupby

def remove_duplicates(sentence):
    # split the sentence into words using regular expressions
    words = re.findall(r'\b\w+\b', sentence)

    # Use dictionary to remove duplicates. At the same time, keep the order using groupby
    words = [next(g) for _, g in groupby(words)]

    # join the words back into a sentence
    sentence = ' '.join(words)

    return sentence