"""
QUESTION:
Create a function `compare_word_sets_order(phrase1: str, phrase2: str)` that compares two input strings, ignoring case and non-alphanumeric characters, to determine if they have the same distinct words in the same sequence. The function should return `True` if the words are identical and in the same order, and `False` otherwise.
"""

import re

def compare_word_sets_order(phrase1: str, phrase2: str):
    # remove non alphanumeric characters
    phrase1 = re.sub('\W+', ' ', phrase1)
    phrase2 = re.sub('\W+', ' ', phrase2)
    
    # convert string to lowercase then split strings into list of words
    phrase1 = phrase1.lower().split() 
    phrase2 = phrase2.lower().split()
    
    # if the lists are not equal in length, return False
    if len(phrase1) != len(phrase2):
        return False
    
    # if the lists are equal in length, compare each pair of words
    for t in zip(phrase1, phrase2):
        if t[0] != t[1]:
            return False
    
    # if all pairs of words are identical, return True
    return True