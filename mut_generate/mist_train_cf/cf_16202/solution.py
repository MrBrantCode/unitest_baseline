"""
QUESTION:
Create a function `word_frequency` that takes a string `text` as input and returns a dictionary where the keys are the words in the text (excluding common English words like "a", "the", and "and") and the values are the frequency of their occurrence. The function should handle text input with multiple paragraphs and accurately count the frequency of words across the entire input.
"""

import re
from collections import defaultdict

def word_frequency(text):
    """
    This function takes a string of text as input and returns a dictionary where the keys are the words in the text 
    (excluding common English words like "a", "the", and "and") and the values are the frequency of their occurrence.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary of word frequencies.
    """

    # Common English words to exclude from the dictionary
    common_words = {"a", "the", "and"}

    # Remove non-alphanumeric characters and split the text into words
    words = re.findall(r'\b\w+\b', text.lower())

    # Create a dictionary to store word frequencies
    word_freq = defaultdict(int)

    # Iterate over each word and count its frequency
    for word in words:
        if word not in common_words:
            word_freq[word] += 1

    return dict(word_freq)