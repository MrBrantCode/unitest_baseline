"""
QUESTION:
Create a function `check_word_identity_and_capitalization(sentence1: str, sentence2: str)` that checks if two sentences have the same set of distinct words with considering capitalization. 

The function should filter non-alphabetical characters and split the sentences into words. It should then count the frequency of each word in both sentences and return True if both sentences have the same sets of distinct words with considering capitalization, and False otherwise.

Note: The function should be case-sensitive, meaning it should consider 'Apple' and 'apple' as two different words.
"""

import re
from collections import Counter

def check_word_identity_and_capitalization(sentence1: str, sentence2: str):
    # filter non-alphabetical characters and split the sentence into words
    words1 = re.findall(r'\b\w+\b', sentence1)
    words2 = re.findall(r'\b\w+\b', sentence2)

    # count frequency of each word in both sentences
    wc1 = Counter(words1)
    wc2 = Counter(words2)

    # both sentences have the same sets of distinct words with considering capitalization, return True. 
    # Otherwise, return False.
    return wc1 == wc2