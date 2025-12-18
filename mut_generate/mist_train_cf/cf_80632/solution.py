"""
QUESTION:
Write a function named `compare_word_sets_frequency_order` that takes two string parameters `phrase1` and `phrase2`. This function should return `True` if the two input phrases contain the same words with the same frequency and in the same order, and `False` otherwise.
"""

def compare_word_sets_frequency_order(phrase1: str, phrase2: str) -> bool:
    """
    Assert if the two input phrases comprise of identical sequences of words, with the same word frequency and order.
    In this case, 'apple' appearing twice consecutively in the first phrase should also appear twice consecutively in 
    the second phrase.
    """
    # Split both phrases into words and compare the resulting lists
    return phrase1.split() == phrase2.split()