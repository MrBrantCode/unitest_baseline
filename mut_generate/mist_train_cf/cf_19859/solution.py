"""
QUESTION:
Remove duplicate words from a given sentence and count the unique words. The function should take a string as input, convert it to lowercase, ignore punctuation marks and special characters, and return a list of unique words and the count of unique words.
"""

import re

def remove_duplicates_and_count(input_sentence):
    """
    Remove duplicate words from a given sentence and count the unique words.

    Args:
        input_sentence (str): The input sentence.

    Returns:
        list: A list of unique words.
        int: The count of unique words.
    """
    # Convert sentence to lowercase
    sentence = input_sentence.lower()

    # Remove punctuation marks and special characters
    sentence = re.sub(r'[^\w\s]', '', sentence)

    # Split sentence into words
    words = sentence.split()

    # Remove duplicate words
    unique_words = list(set(words))

    # Count the number of unique words
    count_unique_words = len(unique_words)

    return unique_words, count_unique_words