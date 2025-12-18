"""
QUESTION:
Write a function `count_unique_words` that takes a text string as input and returns the number of unique words in the text. The function should ignore case, punctuation marks, numbers, and special characters. It should also handle large texts efficiently.

Time Complexity Requirement: O(n), where n is the length of the text.
Space Complexity Requirement: O(m), where m is the number of unique words in the text.
"""

import re
from typing import Set

def count_unique_words(text: str) -> int:
    """
    Returns the number of unique words in the given text, ignoring case, punctuation marks, numbers, and special characters.

    Time Complexity: O(n), where n is the length of the text.
    Space Complexity: O(m), where m is the number of unique words in the text.

    :param text: The input text string.
    :return: The number of unique words in the text.
    """
    
    # Convert the text to lowercase to ignore case sensitivity
    text = text.lower()
    
    # Use a regular expression to extract all the words from the text, ignoring punctuation marks, numbers, and special characters
    words = re.findall(r'\b\w+\b', text)
    
    # Use a set to store unique words, which has an average time complexity of O(1) for insertions
    unique_words: Set[str] = set(words)
    
    # Return the number of unique words
    return len(unique_words)