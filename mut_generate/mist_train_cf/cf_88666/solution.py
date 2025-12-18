"""
QUESTION:
Design a function `count_word_frequency` that takes a list of sentences as input and returns a dictionary containing the frequency of each unique word in the sentences. The function should consider 'Apples' and 'apples' as two different words, and numbers should be treated as separate words.
"""

import re
from collections import defaultdict

def count_word_frequency(sentences):
    frequency_dict = defaultdict(int)
    for sentence in sentences:
        words = re.findall(r'\w+', sentence)
        for word in words:
            frequency_dict[word] += 1
    return dict(frequency_dict)