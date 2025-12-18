"""
QUESTION:
Design a function `count_unique_words` that takes a string paragraph and a boolean case_sensitive as input, and returns the number of unique words in the paragraph. The function should treat 'word' and 'Word' as the same word if case_sensitive is False. The function should ignore punctuation and only consider alphabetic characters.
"""

import re
from collections import Counter

def count_unique_words(paragraph, case_sensitive):
    """
    Counts the number of unique words in a given paragraph.

    Args:
    paragraph (str): The input paragraph.
    case_sensitive (bool): Whether to consider case sensitivity.

    Returns:
    int: The number of unique words in the paragraph.
    """
    
    # Convert to lower case if case_sensitive is False
    if not case_sensitive:
        paragraph = paragraph.lower()

    # Remove non-alphabetic characters and split into words
    words = re.findall(r'\b\w+\b', paragraph)

    # Count unique words
    unique_word_count = len(Counter(words))

    return unique_word_count