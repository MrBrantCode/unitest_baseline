"""
QUESTION:
Design a function `word_frequency` that takes a list of sentences as input, extracts unique words from the sentences while ignoring case sensitivity and punctuation, and returns a dictionary where each key is a unique word and each value is the frequency of the word's occurrence across all sentences. The function should not allow repetitions in the output dictionary.
"""

import re
from collections import defaultdict

def word_frequency(sentences):
    """
    This function calculates the frequency of each word in a list of sentences.

    Args:
        sentences (list): A list of sentences.

    Returns:
        dict: A dictionary where each key is a unique word and each value is the frequency of the word's occurrence.
    """
    frequency = defaultdict(int)
    for sentence in sentences:
        words = re.findall(r'\b\w+\b', sentence.lower())
        for word in words:
            frequency[word] += 1
    return dict(frequency)