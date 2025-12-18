"""
QUESTION:
Design a function `word_frequency` that takes a list of sentences as strings and returns a dictionary containing the frequency of each word in the sentences. Each sentence may contain punctuation and special characters. The output dictionary should be case-sensitive, meaning 'Apples' and 'apples' should be considered as two different words.
"""

import re
from collections import defaultdict

def word_frequency(sentences):
    frequency = defaultdict(int)
    for sentence in sentences:
        words = re.findall(r'\b\w+\b', sentence)
        for word in words:
            frequency[word] += 1
    return dict(frequency)