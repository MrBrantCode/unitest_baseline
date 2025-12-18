"""
QUESTION:
Implement a function named `word_frequency` that takes a string `txt` as input, performs a frequency analysis of all the words in the string, and returns a dictionary containing all distinct words and their counts. The function should be case-insensitive and able to handle punctuation.
"""

import re

def word_frequency(txt):
    freq_dist = {}
    words = re.findall(r'\b\w+\b', txt.lower())
    for word in words:
        freq_dist[word] = freq_dist.get(word, 0) + 1
    return freq_dist