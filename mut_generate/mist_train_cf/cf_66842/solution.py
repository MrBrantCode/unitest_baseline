"""
QUESTION:
Create a function named `compare_word_sets` that takes two parameters, `phrase1` and `phrase2`, both of type string. The function should return a boolean value indicating whether the two input phrases contain the same set of words, disregarding word repetition and case sensitivity.
"""

def compare_word_sets(phrase1: str, phrase2: str) -> bool:
    """
    Ascertain if two distinct groups of words possess an identical set of lexemes, bearing no relation to word repetition or case sensitivity.
    """
    words1 = set(phrase1.lower().split())
    words2 = set(phrase2.lower().split())
    return words1 == words2