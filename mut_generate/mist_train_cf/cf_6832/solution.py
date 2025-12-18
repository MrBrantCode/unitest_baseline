"""
QUESTION:
Create a function `find_words` that takes a string as input and returns a list of words that start with a capital letter and end with the letter "n". The words should only contain letters and should not be followed by a comma or a period.
"""

import re

def find_words(sentence):
    """
    Returns a list of words that start with a capital letter and end with the letter "n".
    The words should only contain letters and should not be followed by a comma or a period.

    Parameters:
    sentence (str): The input string.

    Returns:
    list: A list of words that match the specified pattern.
    """
    pattern = r'\b[A-Z][A-Za-z]*n\b(?![,.])'
    return re.findall(pattern, sentence)