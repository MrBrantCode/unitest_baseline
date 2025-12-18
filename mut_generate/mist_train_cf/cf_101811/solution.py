"""
QUESTION:
Write a function `clean_sentence(sentence)` that takes a string input `sentence` and returns the sentence with any punctuation at the end removed. The function should be able to handle sentences ending with question marks, exclamation marks, periods, or no punctuation at all. Use regular expressions in your solution.
"""

import re

def clean_sentence(sentence):
    """
    Removes any punctuation at the end of the sentence.
    
    Args:
    sentence (str): The input sentence to be cleaned.
    
    Returns:
    str: The sentence with any punctuation at the end removed.
    """
    cleaned_sentence = re.sub(r'[.?!]+$', '', sentence)
    return cleaned_sentence