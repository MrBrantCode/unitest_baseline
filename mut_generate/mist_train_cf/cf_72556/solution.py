"""
QUESTION:
Write a function `count_word_occurrences` that takes a string `paragraph` as input and returns a dictionary where the keys are unique words in the paragraph and the values are their respective counts. The function should be case-insensitive and should ignore punctuation.
"""

import re
from collections import defaultdict

def count_word_occurrences(paragraph):
    """
    This function takes a string paragraph as input and returns a dictionary where 
    the keys are unique words in the paragraph and the values are their respective counts.
    
    The function is case-insensitive and ignores punctuation.

    Args:
        paragraph (str): The input string.

    Returns:
        dict: A dictionary where keys are unique words and values are their counts.
    """
    
    # normalize the string: lower case and remove punctuation
    clean_paragraph = re.sub(r'[^\w\s]', '', paragraph.lower())

    # split the string into words
    words = clean_paragraph.split()

    # count occurrences of each word
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1

    return dict(word_counts)