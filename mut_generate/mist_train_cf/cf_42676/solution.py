"""
QUESTION:
Implement a function named `count_word_occurrences` that takes a string `text` as input and returns a dictionary where the keys are the words in the text and the values are their corresponding counts. The function should be case-insensitive and consider only alphanumeric characters as part of a word.
"""

import re

def count_word_occurrences(text):
    word_counts = {}
    words = re.findall(r'\b\w+\b', text.lower())
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts