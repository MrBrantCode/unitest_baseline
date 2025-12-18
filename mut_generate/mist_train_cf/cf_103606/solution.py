"""
QUESTION:
Write a function `count_unique_words` that takes a string `passage` as input and returns the number of unique words in the passage. A word is defined as a sequence of characters separated by whitespace, words are case-insensitive, and punctuation marks should not be considered part of a word.
"""

import string

def count_unique_words(passage):
    """
    Returns the number of unique words in the given passage.

    Args:
    passage (str): The input string.

    Returns:
    int: The number of unique words in the passage.
    """
    
    # Convert passage to lowercase
    passage = passage.lower()

    # Remove punctuation marks
    passage = passage.translate(str.maketrans("", "", string.punctuation))

    # Split passage into words
    words = passage.split()

    # Convert list of words to set
    unique_words = set(words)

    # Get number of unique words
    return len(unique_words)