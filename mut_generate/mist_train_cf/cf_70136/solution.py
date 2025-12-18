"""
QUESTION:
Create a function `verify_same_word_sets_freqs` that takes two string parameters, `phrase1` and `phrase2`, and returns a boolean value indicating whether the two strings contain the same set of words with identical frequencies, disregarding word order and case sensitivity.
"""

from collections import Counter

def verify_same_word_sets_freqs(phrase1: str, phrase2: str):
    map1 = Counter(phrase1.lower().split())
    map2 = Counter(phrase2.lower().split())
    return map1 == map2