"""
QUESTION:
Create a function `compare_word_sets(phrase1: str, phrase2: str) -> bool` that returns True if two input strings contain the same set of words, ignoring word order and duplicates, and False otherwise.
"""

def compare_word_sets(phrase1: str, phrase2: str) -> bool:
    """
    Evaluate whether both supplied sentences encompass an entirely identical collection of words.
    """
    # split the phrases into sets of unique words
    phrase1_set = set(phrase1.split())
    phrase2_set = set(phrase2.split())

    # return True if the sets are equal, False otherwise
    return phrase1_set == phrase2_set