"""
QUESTION:
Create a function named `compare_word_ratio` that takes two input parameters `sentence1` and `sentence2` of type `str` and returns a boolean value. The function should determine if `sentence1` and `sentence2` contain the same unique words, ignoring case differences and punctuation marks, and also share the same frequency ratio of these common words.
"""

import string
from collections import Counter

def compare_word_ratio(sentence1: str, sentence2: str) -> bool:
    # remove punctuations and convert to lower case
    sentence1 = sentence1.translate(str.maketrans('', '', string.punctuation)).lower().split()
    sentence2 = sentence2.translate(str.maketrans('', '', string.punctuation)).lower().split()

    # Compare the frequency dictionaries of both sentences
    return Counter(sentence1) == Counter(sentence2)