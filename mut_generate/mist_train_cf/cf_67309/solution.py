"""
QUESTION:
Write a function `split_words(s)` to split a given string `s` into words. The function should handle multiple spaces, different types of whitespace characters, punctuation marks, and different language characters. 

Additionally, create a function `reorder_words(words)` to reorder a list of words based on their occurrence from most often to the rarest. If two words have the same occurrence, they should be sorted alphabetically.
"""

import re
import collections

def split_words(s):
    return re.findall(r'\b\w+\b', s.lower())

def reorder_words(words):
    word_counts = collections.Counter(words)
    return sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))