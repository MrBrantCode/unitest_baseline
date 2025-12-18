"""
QUESTION:
Design a function named `word_frequency` that takes a list of sentences as strings and returns a dictionary containing the frequency of each word in the sentences. The function should consider 'Apples' and 'apples' as two different words, and numbers should also be treated as separate words. The function should also exclude any punctuation, special characters.
"""

import re

def word_frequency(sentences):
    word_count = {}
    for sentence in sentences:
        words = re.findall(r'\b\w+\b', sentence)
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count