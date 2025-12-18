"""
QUESTION:
Write a function `word_frequency` that takes a string `text` as input, removes non-alphanumeric characters, excludes common stop words, counts the occurrences of each word, and returns a dictionary with the word frequencies in descending order. The function should be case-insensitive and consider 'is', 'a', 'this', 'of', 'the', 'and', 'to' as stop words.
"""

import re
from collections import Counter

def word_frequency(text):
    """
    This function calculates the frequency of each word in a given text, 
    removing non-alphanumeric characters and common stop words.

    Args:
    text (str): The input text.

    Returns:
    dict: A dictionary with word frequencies in descending order.
    """

    # Remove non-alphanumeric characters
    clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())

    # Split the text into words
    words = clean_text.split()

    # Define common stop words to exclude from word count
    stop_words = ['is', 'a', 'this', 'of', 'the', 'and', 'to']

    # Count the occurrences of each word
    word_count = Counter(word for word in words if word not in stop_words)

    # Return the word count in descending order of frequency
    return dict(word_count.most_common())