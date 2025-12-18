"""
QUESTION:
Write a function named `shannon_entropy` that calculates the Shannon entropy of a given string. The function should take a string as input and return the Shannon entropy value. The entropy should be calculated using the formula: -sum(freq * log2(freq)) where freq is the frequency of each character in the string divided by the total number of characters.
"""

import math
from collections import Counter

def shannon_entropy(string):
    freq_dict = Counter(string)
    total_chars = len(string)
    entropy = 0
    for char_freq in freq_dict.values():
        freq = char_freq / total_chars
        entropy += freq * math.log2(freq)
    return -entropy