"""
QUESTION:
Write a function match_cat_sentences that uses a regex expression to match sentences with the word "cat" followed by any number of characters except the letter "z" and ends with a period. The function should return True if a match is found and False otherwise.
"""

import re

def match_cat_sentences(sentence):
    """
    This function uses a regex expression to match sentences with the word "cat" 
    followed by any number of characters except the letter "z" and ends with a period.
    
    Args:
        sentence (str): The input sentence to be matched.
    
    Returns:
        bool: True if a match is found, False otherwise.
    """
    pattern = r'\bcat[^z]*\.'
    return bool(re.search(pattern, sentence))