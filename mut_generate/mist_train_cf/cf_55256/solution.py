"""
QUESTION:
Create a function `compare_word_sets_order(phrase1: str, phrase2: str) -> bool` that takes two string inputs, `phrase1` and `phrase2`. The function should return `True` if the two phrases contain the same unique words, ignoring case and any non-alphanumeric characters, and if the same words appear in an identical order. Otherwise, it should return `False`.
"""

import re

def compare_word_sets_order(phrase1: str, phrase2: str) -> bool:
    # Remove non-alphanumeric characters and split phrase into words, and convert to lower case
    phrase1_words = [re.sub(r'\W+', '', word).lower() for word in phrase1.split()]
    phrase2_words = [re.sub(r'\W+', '', word).lower() for word in phrase2.split()]

    # Compare the two lists of words
    return phrase1_words == phrase2_words