"""
QUESTION:
Create a function called `word_count` that calculates the aggregate quantity of individual words in a provided literary excerpt, considering case insensitivity and punctuation. The function should take a string of text as input and return a dictionary with words as keys and their respective counts as values.
"""

import string
from collections import Counter

def word_count(text):
    """
    Calculate the aggregate quantity of individual words in a provided literary excerpt.

    Args:
    text (str): A string of text.

    Returns:
    dict: A dictionary with words as keys and their respective counts as values.
    """
    text_no_punct = text.translate(str.maketrans('', '', string.punctuation))
    words = text_no_punct.lower().split()
    return Counter(words)