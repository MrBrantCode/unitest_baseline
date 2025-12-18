"""
QUESTION:
Create a function `parse_words` that takes a sentence as input and returns a list of words. The function should use regular expressions to parse the sentence into individual words. The input sentence can contain any combination of letters, spaces, and punctuation.
"""

import re

def parse_words(sentence):
    """
    Parse a sentence into individual words using regular expressions.
    
    Args:
        sentence (str): The input sentence.
    
    Returns:
        list: A list of words.
    """
    return re.findall(r'\w+', sentence)