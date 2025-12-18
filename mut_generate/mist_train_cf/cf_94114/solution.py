"""
QUESTION:
Create a function `word_frequency` that takes a string of text as input, counts the frequency of each word excluding common English words ("a", "the", "and"), and returns a dictionary where the keys are the words and the values are their frequencies. The function should handle text input with multiple paragraphs and accurately count the frequency of words across the entire input.
"""

import re
from collections import defaultdict

def word_frequency(text):
    """
    Counts the frequency of each word in a given text, excluding common English words.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary where the keys are the words and the values are their frequencies.
    """
    common_words = {"a", "the", "and"}
    words = re.findall(r'\b\w+\b', text.lower())
    word_freq = defaultdict(int)
    for word in words:
        if word not in common_words:
            word_freq[word] += 1
    return dict(word_freq)