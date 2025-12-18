"""
QUESTION:
Extract words from a given sentence, convert them to uppercase, count the frequency of each word, and return the words in descending order of their frequency. Use a function called `extract_and_sort_words` and write it to take a string input `sentence`. Assume that the input sentence is a string of words separated by spaces and/or punctuation.
"""

import re
from collections import Counter

def extract_and_sort_words(sentence):
    """
    Extract words from a given sentence, convert them to uppercase, 
    count the frequency of each word, and return the words in descending 
    order of their frequency.

    Args:
        sentence (str): The input sentence.

    Returns:
        list: A list of tuples containing each word in uppercase and its frequency, 
              sorted in descending order of frequency.
    """
    # Extract words using regex
    words = re.findall(r'\b\w+\b', sentence)

    # Convert to uppercase
    words_uppercase = [word.upper() for word in words]

    # Count the frequency of each word
    word_frequency = Counter(words_uppercase)

    # Sort words in descending order of frequency
    sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

    return sorted_words