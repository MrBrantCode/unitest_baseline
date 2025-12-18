"""
QUESTION:
Write a function named `parse_string` that takes an input string and returns a dictionary containing each word and its frequency, excluding common English stop words and words that are part of longer words. The function should handle large input strings by processing them in chunks or lines, and convert all words to lowercase. The stop words list should include 'the', 'and', 'or', 'is', 'a', 'how', 'are', 'you', 'doing', 'today', 'weather', 'nice'.
"""

import re

def parse_string(input_string):
    stop_words = ['the', 'and', 'or', 'is', 'a', 'how', 'are', 'you', 'doing', 'today', 'weather', 'nice']
    word_frequency = {}

    # Process the input string in chunks or lines to avoid memory issues
    for line in input_string.split('\n'):
        words = re.findall(r'\b[a-zA-Z]+\b', line.lower())

        for word in words:
            if word not in stop_words and word not in word_frequency:
                word_frequency[word] = 1
            elif word not in stop_words:
                word_frequency[word] += 1

    return word_frequency