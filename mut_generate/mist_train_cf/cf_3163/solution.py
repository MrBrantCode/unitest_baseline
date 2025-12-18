"""
QUESTION:
Create a function `word_frequency` that takes a string as input, converts it to uppercase, removes punctuation marks, counts the frequency of each word, and returns the words in descending order of their frequency. The function should only count each word once, regardless of its original case or punctuation, and the output should be case-insensitive. The function should return a list of tuples, where each tuple contains a word and its frequency.
"""

import re
from collections import Counter

def word_frequency(text):
    """
    This function takes a string as input, converts it to uppercase, removes punctuation marks, 
    counts the frequency of each word, and returns the words in descending order of their frequency.

    Args:
        text (str): The input string.

    Returns:
        list: A list of tuples, where each tuple contains a word and its frequency.
    """

    # Convert to uppercase and remove punctuation marks
    text = re.sub(r'[^\w\s]', '', text.upper())

    # Count the frequency of each word
    word_count = Counter(text.split())

    # Sort the words in descending order of their frequency
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_words