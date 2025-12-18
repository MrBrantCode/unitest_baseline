"""
QUESTION:
Create a function called `word_count` that takes a string `paragraph` as input. The function should use regular expressions and data structures to extract, count, and sort the instances of each unique word in the paragraph. The output should display each word and its count in descending order of occurrence, ignoring case sensitivity.
"""

import re
from collections import Counter

def word_count(paragraph):
    """
    This function takes a string paragraph as input, extracts and counts each unique word 
    (ignoring case sensitivity), and returns the words along with their counts in descending order.

    Args:
        paragraph (str): The input string.

    Returns:
        list[tuple[str, int]]: A list of tuples containing each word and its count.
    """

    # Clean and split the paragraph into words
    words = re.findall(r'\b\w+\b', paragraph.lower())

    # Count the occurrence of each word
    word_count = Counter(words)

    # Sort the words by occurrence
    sorted_words = sorted(word_count.items(), key=lambda pair: pair[1], reverse=True)

    return sorted_words