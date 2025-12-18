"""
QUESTION:
Create a function named `count_words` that takes a string as input and returns a dictionary where the keys are unique words from the string (case-insensitive and ignoring punctuation marks, special characters, and numbers are treated as words) and the values are the number of occurrences of each word.
"""

import re
from collections import defaultdict

def count_words(string):
    # Convert the string to lowercase and split into words
    words = re.findall(r'\w+', string.lower())

    # Count the occurrences of each word using a defaultdict
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1

    # Convert the defaultdict to a regular dictionary
    word_count = dict(word_count)

    return word_count