"""
QUESTION:
Create a function called `count_words` that takes a string and an optional list of words to exclude, then returns a dictionary-like object containing the count of each unique word in the string excluding common words ("the", "a", "is", "and", "of", "in") and the provided excluded words. The function should be case-insensitive and consider punctuation as word boundaries.
"""

import re
from collections import Counter

def count_words(string, exclude_words=[]):
    common_words = set(['the', 'a', 'is', 'and', 'of', 'in'])
    common_words = common_words.union(exclude_words)
    words = re.findall(r'\b\w+\b', string.lower())
    word_count = Counter(word for word in words if word not in common_words)
    return word_count