"""
QUESTION:
Write a Python function named `clean_sentence` that takes a sentence as input and returns the sentence with any trailing punctuation (question mark, exclamation mark, or period) removed.
"""

import re

def clean_sentence(sentence):
    """
    Removes any trailing punctuation (question mark, exclamation mark, or period) from the input sentence.

    Args:
    sentence (str): The input sentence.

    Returns:
    str: The sentence with any trailing punctuation removed.
    """
    cleaned_sentence = re.sub(r'[.?!]+$', '', sentence)
    return cleaned_sentence