"""
QUESTION:
Write a function named `word_frequency` that takes a string `narrative` as input, and returns a dictionary where keys are the unique words in the narrative and values are their corresponding frequencies. The function should ignore case and consider punctuation as word separators.
"""

import re
from collections import Counter

def word_frequency(narrative):
    """
    This function calculates the frequency of each unique word in the given narrative.

    Args:
        narrative (str): The input string for which word frequency needs to be calculated.

    Returns:
        dict: A dictionary where keys are the unique words in the narrative and values are their corresponding frequencies.
    """
    words = re.findall('\w+', narrative.lower())
    return Counter(words)