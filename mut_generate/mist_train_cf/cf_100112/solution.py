"""
QUESTION:
Create a function called `sorted_words` that takes a list of words as input, removes any duplicates, excludes words with more than six letters, converts the words to lowercase, and returns the result in ascending order. The function should use a list comprehension and built-in functions for sorting and removing duplicates.
"""

def sorted_words(words):
    """
    Removes duplicates, excludes words with more than six letters, 
    converts the words to lowercase, and returns the result in ascending order.

    Args:
    words (list): A list of words

    Returns:
    list: A sorted list of words
    """
    return sorted([word.lower() for word in set(words) if len(word) <= 6])