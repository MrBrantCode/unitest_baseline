"""
QUESTION:
Create a function `count_words` that takes a sentence as input and returns a dictionary where keys are distinct words in the sentence and values are their frequency. The function should ignore punctuation marks and treat lowercase and uppercase versions of the same word as distinct words.
"""

import collections
import re

def count_words(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    return dict(collections.Counter(words))