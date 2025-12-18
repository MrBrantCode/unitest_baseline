"""
QUESTION:
Create a function named `compare_word_sets` that takes two string arguments `phrase1` and `phrase2`. The function should return `True` if the two phrases contain identical non-repeating words, regardless of order, and `False` otherwise. The function should ignore duplicates within each phrase and consider the phrases as case-sensitive.
"""

def compare_word_sets(phrase1: str, phrase2: str) -> bool:
    set1 = set(phrase1.split())
    set2 = set(phrase2.split())
    return set1 == set2