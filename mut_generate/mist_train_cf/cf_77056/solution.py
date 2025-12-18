"""
QUESTION:
Create a function named `compare_word_sets` that takes two string parameters `phrase1` and `phrase2` and returns a boolean value indicating whether the two strings contain the same unique words, regardless of their order or frequency. The function should consider words as case-sensitive and should not normalize the case of the words.
"""

def compare_word_sets(phrase1: str, phrase2: str) -> bool:
    return set(phrase1.split()) == set(phrase2.split())