"""
QUESTION:
Write a function `compare_word_sets(phrase1: str, phrase2: str)` that compares two phrases and returns a boolean indicating whether they contain the same unique words, regardless of their order or frequency.
"""

def compare_word_sets(phrase1: str, phrase2: str) -> bool:
    set1 = set(phrase1.split())
    set2 = set(phrase2.split())
    return set1 == set2