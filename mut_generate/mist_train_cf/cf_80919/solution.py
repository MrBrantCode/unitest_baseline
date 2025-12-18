"""
QUESTION:
Construct a function named `get_sentences` that takes a list of strings as input and returns a list of sentences that start with the phrase "I like" and end with a full stop, exclamation mark, or question mark, but do not contain the word "dislike".
"""

import re

def get_sentences(text):
    """
    This function takes a list of strings as input and returns a list of sentences 
    that start with the phrase "I like" and end with a full stop, exclamation mark, 
    or question mark, but do not contain the word "dislike".
    
    Parameters:
    text (list): A list of strings.
    
    Returns:
    list: A list of sentences that match the specified criteria.
    """
    
    pattern = r'I like(?!.*dislike).*[.!?]'
    sentences = [t for t in text if re.match(pattern, t)]
    return sentences