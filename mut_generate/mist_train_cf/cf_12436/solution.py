"""
QUESTION:
Write a function `remove_duplicates` that takes a string as input, converts it to lowercase, removes duplicate words, and returns a set of unique words along with the count of unique words. The function should use regular expressions to extract words from the string, considering a word as one or more word characters.
"""

import re

def remove_duplicates(sentence):
    """
    This function takes a string as input, converts it to lowercase, removes duplicate words, 
    and returns a set of unique words along with the count of unique words.

    Args:
        sentence (str): The input string.

    Returns:
        tuple: A set of unique words and the count of unique words.
    """

    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Remove duplicate words
    unique_words = set(re.findall(r'\b\w+\b', sentence))

    # Count the number of unique words
    num_unique_words = len(unique_words)

    return unique_words, num_unique_words