"""
QUESTION:
Write a function named `match_the_quick` that takes a sentence as input and returns a list of substrings that match 'the' followed by 'quick' and preceded by a word that starts with a capital letter. The function should use regex and the matched substring should not be part of a larger word.
"""

import re

def match_the_quick(sentence):
    """
    Returns a list of substrings that match 'the' followed by 'quick' and preceded by a word that starts with a capital letter.
    
    Args:
        sentence (str): The input sentence to search for the pattern.
    
    Returns:
        list: A list of substrings that match the pattern.
    """
    pattern = r'\b[A-Z][a-zA-Z]* the quick\b'
    matches = re.findall(pattern, sentence)
    return matches