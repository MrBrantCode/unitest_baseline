"""
QUESTION:
Write a function called `most_frequent_word` that takes a string of text as input and returns the most frequently occurring word in the text. The words are case-insensitive and punctuation should be ignored.
"""

import re
from collections import Counter

def most_frequent_word(text):
    """
    Returns the most frequently occurring word in the given text.

    The words are case-insensitive and punctuation is ignored.

    Args:
        text (str): The input text.

    Returns:
        str: The most frequently occurring word.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(1)[0][0]