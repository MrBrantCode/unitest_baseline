"""
QUESTION:
Write a function named `parse_string` that takes a string as input, parses it, and returns a dictionary where each key is a word from the string and the corresponding value is its frequency. The function should exclude common English stop words ('the', 'and', 'or', 'is', 'a', 'how', 'are', 'you', 'doing', 'today', 'weather', 'nice') and words that are part of longer words. The function should convert all words to lowercase and handle large input strings by processing them in chunks or lines to avoid memory issues.
"""

import re

def parse_string(input_string):
    stop_words = ['the', 'and', 'or', 'is', 'a', 'how', 'are', 'you', 'doing', 'today', 'weather', 'nice']
    word_frequency = {}

    for line in input_string.split('\n'):
        words = re.findall(r'\b[a-zA-Z]+\b', line.lower())

        for word in words:
            if word not in stop_words and word not in word_frequency:
                word_frequency[word] = 1
            elif word not in stop_words:
                word_frequency[word] += 1

    return word_frequency