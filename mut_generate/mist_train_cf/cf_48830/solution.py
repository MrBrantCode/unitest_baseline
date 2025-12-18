"""
QUESTION:
Write a function `is_pangram` that accepts a string input and returns a boolean value indicating if the given string is a pangram, which is a sentence that uses every letter of the alphabet at least once, in a case-insensitive manner. The function should handle errors gracefully and have a time complexity better than O(n²). Additionally, create a function `multiple_pangram` that accepts a list of strings and returns a list of booleans corresponding to whether each provided sentence is a pangram.
"""

def is_pangram(sentence):
    """
    Checks if a given sentence is a pangram.

    Args:
        sentence (str): The input sentence to check.

    Returns:
        bool: True if the sentence is a pangram, False otherwise.
    """
    return set('abcdefghijklmnopqrstuvwxyz') <= set(sentence.lower())