"""
QUESTION:
Create a function `sort_unique_chars` that takes a string of lowercase alphabets as input, sorts the characters in ascending order, and returns a list of unique characters.
"""

def sort_unique_chars(s):
    """
    Sorts the unique characters in a string of lowercase alphabets in ascending order.

    Args:
        s (str): The input string.

    Returns:
        list: A list of unique characters in ascending order.
    """
    return sorted(set(s))