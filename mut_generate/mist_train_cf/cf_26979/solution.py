"""
QUESTION:
Implement a function named `word_frequency` that takes a string of text as input, and returns a dictionary containing the frequency of each word in the text. The function should be case-insensitive, ignore punctuation marks, and only consider alphanumeric characters and spaces as part of the words. The output dictionary should not contain any words with a frequency of 0.
"""

import re

def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return {word: freq for word, freq in frequency.items() if freq > 0}