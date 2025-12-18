"""
QUESTION:
Create a function called `compare_word_sets_order` that takes two strings as input, disregards case sensitivity and non-alphanumeric entities, and returns `True` if the strings contain the same unique words in the same order, and `False` otherwise.
"""

import re

def compare_word_sets_order(phrase1: str, phrase2: str) -> bool:
    phrase1 = re.sub(r'\W+', ' ', phrase1).lower()
    phrase2 = re.sub(r'\W+', ' ', phrase2).lower()
    
    word_list1 = phrase1.split()
    word_list2 = phrase2.split()
    
    return word_list1 == word_list2