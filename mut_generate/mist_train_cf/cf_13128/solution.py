"""
QUESTION:
Write a function called `estimate_unique_words` that takes a string `text` as input and returns the estimated number of unique words in the text. The function should handle large texts efficiently and have a time complexity of O(n), where n is the length of the text, and a space complexity of O(m), where m is the number of unique words in the text. The function should ignore case, punctuation marks, numbers, and special characters when counting unique words.
"""

import re

def estimate_unique_words(text):
    """
    Estimates the number of unique words in the given text.

    Args:
    text (str): The input text.

    Returns:
    int: The estimated number of unique words in the text.
    """
    unique_words = set()
    for word in text.split():
        cleaned_word = re.sub(r'[^a-zA-Z]', '', word).lower()
        if cleaned_word:
            unique_words.add(cleaned_word)
    return len(unique_words)