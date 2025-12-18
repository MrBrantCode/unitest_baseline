"""
QUESTION:
Create a function named `interleave_strings(word1, word2, word3)` that takes three strings as input, each consisting of lowercase English letters. Interleave the strings by adding letters in the order of `word1`, `word2`, and `word3`. If a string is shorter than the others, skip to the next string once it's exhausted, and if a string is longer than the others, append the additional letters onto the end of the interleaved string. Return a tuple containing the interleaved string and a dictionary with each character as the key and the number of times it appears as the value. The input strings are guaranteed to be between 1 and 1000 characters in length.
"""

from collections import Counter
from itertools import zip_longest

def interleave_strings(word1, word2, word3):
    res = []
    for a, b, c in zip_longest(word1, word2, word3, fillvalue=''):
        res.extend([a, b, c])
    merged = ''.join(res)
    return merged, dict(Counter(merged))