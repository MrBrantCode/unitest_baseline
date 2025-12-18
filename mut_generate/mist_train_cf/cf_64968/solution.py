"""
QUESTION:
Implement a function named `check_word_identicality_and_capitalization(sentence1: str, sentence2: str)` that checks if two input strings have the same set of distinct words, disregarding non-alphabetical characters, but considering their original capitalization. The function should return True if the two strings meet the condition and False otherwise.
"""

import re
from collections import Counter

def check_word_identicality_and_capitalization(sentence1: str, sentence2: str):
    """
    Checks if two input strings have the same set of distinct words, disregarding non-alphabetical characters, 
    but considering their original capitalization.

    Args:
    sentence1 (str): The first input sentence.
    sentence2 (str): The second input sentence.

    Returns:
    bool: True if the two strings meet the condition, False otherwise.
    """
    
    # filter non-alphabetical characters and split the sentence into words
    words1 = re.findall(r'\b\w+\b', sentence1)
    words2 = re.findall(r'\b\w+\b', sentence2)

    # count frequency of each word in both sentences
    wc1 = Counter(words1)
    wc2 = Counter(words2)

    # both sentences have the same sets of distinct words with considering capitalization, return True
    # otherwise, return False
    return wc1 == wc2