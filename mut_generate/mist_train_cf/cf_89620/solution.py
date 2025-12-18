"""
QUESTION:
Write a function `find_words` that uses a regular expression in Python to find all words in a given sentence that start with a capital letter and end with "n", excluding any words containing numbers or special characters. The function should also ignore any words followed by a comma or a period.
"""

import re

def find_words(sentence):
    """
    This function uses a regular expression to find all words in a given sentence 
    that start with a capital letter and end with "n", excluding any words containing 
    numbers or special characters. The function also ignores any words followed by a comma or a period.

    Parameters:
    sentence (str): The input sentence to search for words.

    Returns:
    list: A list of words that match the specified pattern.
    """
    pattern = r'\b[A-Z][A-Za-z]*n\b(?![,.])'
    return re.findall(pattern, sentence)