"""
QUESTION:
Create a function called `filter_and_sort_words` that takes a list of words as input and returns a list of words that are four or more characters in length, sorted in alphabetical order. The function should not take any other parameters.
"""

def filter_and_sort_words(words):
    """
    Returns a list of words that are four or more characters in length, sorted in alphabetical order.

    Args:
        words (list): A list of words

    Returns:
        list: A list of filtered and sorted words
    """
    return sorted([word for word in words if len(word) >= 4])