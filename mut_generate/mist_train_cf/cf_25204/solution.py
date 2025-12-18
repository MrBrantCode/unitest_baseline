"""
QUESTION:
Write a function `replace_punctuation` that replaces all punctuation marks in a given sentence with underscores.
"""

import string

def replace_punctuation(sentence):
    """
    Replaces all punctuation marks in a given sentence with underscores.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The sentence with all punctuation marks replaced with underscores.
    """
    translator = str.maketrans(string.punctuation, '_' * len(string.punctuation))
    return sentence.translate(translator)