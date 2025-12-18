"""
QUESTION:
Write a function `word_count(word_string)` that takes a string of words and returns a dictionary-like object containing the count of each word, excluding common English stop words. The function should ignore case sensitivity, handle punctuation marks and special characters properly, and be able to handle very large input strings efficiently.
"""

import re
from collections import Counter

def word_count(word_string):
    words = re.findall(r'\w+', word_string.lower())
    stop_words = ['a', 'an', 'the', 'is', 'of', 'etc.']
    word_counts = Counter(word for word in words if word not in stop_words)
    return word_counts