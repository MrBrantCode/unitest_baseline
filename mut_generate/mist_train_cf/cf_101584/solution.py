"""
QUESTION:
Write a function named `clean_sentence` that takes a string `sentence` as input and returns the sentence with all words that start with a lowercase letter and are followed by a space removed. Use regular expressions to achieve this. The function should not take any additional parameters.
"""

import re

def clean_sentence(sentence):
    """
    Removes all words that start with a lowercase letter and are followed by a space from a sentence.
    
    Args:
    sentence (str): The input sentence.
    
    Returns:
    str: The sentence with unnecessary words removed.
    """
    pattern = r'\b[a-z]+ '
    return re.sub(pattern, '', sentence)