"""
QUESTION:
Write a function `reverse_text_order` that takes a list of words as input and returns the list in reverse order. Implement a unit testing suite using the `unittest` module to test the function. The testing suite should cover at least the following cases: regular case with multiple words, regular case with a single word, empty list, and a list with duplicate words.
"""

def reverse_text_order(words):
    """
    This function takes a list of words and returns them in reverse order.
    """
    return words[::-1]