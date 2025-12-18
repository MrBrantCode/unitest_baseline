"""
QUESTION:
Write a function `perm_check(sentence)` that checks if the input sentence is a permutation of the aphorism "You can't judge a book by its cover". The function should ignore case sensitivity and non-word characters. It should return True if the sentence is a permutation of the aphorism, and False otherwise.
"""

import re
from collections import Counter

def perm_check(sentence):
    aphorism = 'You can\'t judge a book by its cover'

    # Normalize both aphorism and target sentence
    aphorism = re.sub(r'[^\w\s]','',aphorism).lower().split()
    sentence = re.sub(r'[^\w\s]','',sentence).lower().split()

    # Return True if the sorted list of words in the aphorism and 
    # sentence are the same, otherwise return False
    return Counter(aphorism) == Counter(sentence)