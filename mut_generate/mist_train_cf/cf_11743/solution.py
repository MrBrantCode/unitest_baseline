"""
QUESTION:
Create a function named `find_bn_words` that utilizes a regular expression to match all words that begin with 'b' and end with 'n' in a given text, regardless of case. The function should take a string as input and return a list of matching words. The input text may contain multiple sentences and special characters.
"""

import re

def find_bn_words(text):
    """
    Find all words in the given text that begin with 'b' and end with 'n', 
    regardless of case.

    Args:
    text (str): The input text to search for matching words.

    Returns:
    list: A list of words that match the specified pattern.
    """
    pattern = r"\b[bB]\w*n\b"
    return re.findall(pattern, text)