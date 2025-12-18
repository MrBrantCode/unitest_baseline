"""
QUESTION:
Write a function `word_length` that takes a string of words as input, calculates the length of each word, and returns an array of word lengths. The input string may contain multiple words separated by spaces.
"""

def word_length(s):
    """
    Calculate the length of each word in a string.

    Args:
        s (str): The input string.

    Returns:
        list: A list of word lengths.
    """
    return [len(word) for word in s.split()]