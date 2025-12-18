"""
QUESTION:
Create a function `compare_word_sequence(phrase1, phrase2)` that compares two phrases considering word multiplicity, case insensitivity, punctuation, and the arrangement of words. The function should return `True` if the phrases are equal and `False` otherwise. The function should ignore punctuation and be case insensitive.
"""

import string

def compare_word_sequence(phrase1: str, phrase2: str) -> bool:
    normalized_phrase1 = ''.join(ch for ch in phrase1 if ch not in string.punctuation).lower().split()
    normalized_phrase2 = ''.join(ch for ch in phrase2 if ch not in string.punctuation).lower().split()

    return normalized_phrase1 == normalized_phrase2