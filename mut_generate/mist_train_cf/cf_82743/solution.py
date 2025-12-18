"""
QUESTION:
Write a function called `compare_word_permutations` that takes two strings `phrase1` and `phrase2` as input, and returns `True` if the two phrases contain the same unique words regardless of order and case, and `False` otherwise. The function should disregard punctuation and consider words as case-insensitive.
"""

import re

def compare_word_permutations(phrase1: str, phrase2: str) -> bool:
    phrase1 = set(re.sub(r'\W+', ' ', phrase1).lower().split())  # Removing punctuations and converting to set
    phrase2 = set(re.sub(r'\W+', ' ', phrase2).lower().split())  # Removing punctuations and converting to set

    return phrase1 == phrase2