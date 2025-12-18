"""
QUESTION:
Create a function called `sorted_words` that takes a list of words as input and returns a list of words that are in ascending order, contain only lowercase letters, have six letters or less, and contain no duplicates.
"""

def sorted_words(words):
    """
    Returns a list of words that are in ascending order, contain only lowercase letters, 
    have six letters or less, and contain no duplicates.

    Args:
        words (list): A list of words.

    Returns:
        list: A list of filtered and sorted words.
    """
    return sorted([word.lower() for word in set(words) if len(word) <= 6])