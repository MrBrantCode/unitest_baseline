"""
QUESTION:
Write a function `count_unique_words` that takes a paragraph of text as input and returns a dictionary where the keys are unique words and the values are their corresponding counts. The function should consider words with apostrophes as separate entities and ignore case when matching words.
"""

import re
from collections import Counter

def count_unique_words(paragraph):
    """
    This function takes a paragraph of text as input and returns a dictionary 
    where the keys are unique words and the values are their corresponding counts.

    Args:
        paragraph (str): The input paragraph of text.

    Returns:
        dict: A dictionary with unique words as keys and their counts as values.
    """

    # Use regular expression to break text into words
    words = re.findall(r"(?u)\b\w+\b", paragraph.lower())

    # Use collections.Counter to count unique instances
    count = Counter(words)

    return count