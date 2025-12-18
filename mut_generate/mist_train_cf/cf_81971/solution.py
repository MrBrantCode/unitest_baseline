"""
QUESTION:
Create a function named `compare_word_sets` that takes two strings `phrase1` and `phrase2` as input and returns a boolean value indicating whether both strings contain exactly the same set of unique words, regardless of word count and order.
"""

def compare_word_sets(phrase1: str, phrase2: str) -> bool:
    """
    Determine whether the two input sentences contain an exactly identical set of words irrespective of word count.
    """
    return set(phrase1.split()) == set(phrase2.split())