"""
QUESTION:
Create a function `sort_words` that takes a list of words as input. The function should sort the list in descending order based on the length of each word. If two or more words have the same length, they should be sorted in alphabetical order.
"""

def sort_words(words):
    """
    Sorts a list of words in descending order based on their length.
    If two or more words have the same length, they are sorted in alphabetical order.

    Args:
        words (list): A list of words

    Returns:
        list: A sorted list of words
    """
    return sorted(words, key=lambda x: (-len(x), x))