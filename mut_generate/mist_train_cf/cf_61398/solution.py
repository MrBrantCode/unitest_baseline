"""
QUESTION:
Create a function `compare_word_sets(phrase1: str, phrase2: str)` that takes two phrases as input and returns a boolean indicating whether the two phrases contain the same collection of words, regardless of order or frequency. The function should consider a word as any sequence of characters separated by spaces.
"""

def compare_word_sets(phrase1: str, phrase2: str):
    words1 = set(phrase1.split())
    words2 = set(phrase2.split())
    return words1 == words2