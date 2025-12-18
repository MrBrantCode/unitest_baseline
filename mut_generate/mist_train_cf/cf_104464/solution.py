"""
QUESTION:
Write a function `sort_words_by_length` that takes a sentence as input, splits it into individual words, and returns the words sorted by their length in descending order. The time complexity should be O(n log n) or better.
"""

def sort_words_by_length(sentence):
    """
    This function takes a sentence as input, splits it into individual words, 
    and returns the words sorted by their length in descending order.

    Parameters:
    sentence (str): The input sentence.

    Returns:
    list: A list of words sorted by their length in descending order.
    """
    return sorted(sentence.split(), key=lambda x: len(x), reverse=True)