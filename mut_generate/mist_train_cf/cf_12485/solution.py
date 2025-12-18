"""
QUESTION:
Write a function `extract_sion_words` that takes a string `text` as input and returns a list of words that end with 'sion'. The function should use regular expression to match the words, ensuring they are preceded by a space or a punctuation mark and followed by a space or a punctuation mark. The function should be case-insensitive and return the extracted words in alphabetical order. The input string can contain up to 500 words.
"""

import re

def extract_sion_words(text):
    """
    Extracts words that end with 'sion' from a given text.

    Args:
    text (str): The input text to extract words from.

    Returns:
    list: A list of words that end with 'sion' in alphabetical order.
    """
    # Find all words ending with 'sion'
    matches = re.findall(r'\b[A-Za-z]+sion\b', text, re.IGNORECASE)

    # Sort the extracted words in alphabetical order
    matches = sorted(matches)

    return matches