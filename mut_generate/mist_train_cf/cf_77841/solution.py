"""
QUESTION:
Design a function `count_chars` that takes a string `s` as input and returns a dictionary with the three most frequent characters and their frequencies, excluding spaces and punctuation. If the string has fewer than three unique characters, the function should return an error message.
"""

import collections
import re

def count_chars(s):
    s = re.sub('[\W_]+', '', s).lower()  # exclude spaces and punctuation, case-insensitive
    counts = collections.Counter(s)
    
    if len(counts) < 3:
        return "Error: Not enough unique characters."
    
    return dict(counts.most_common(3))