"""
QUESTION:
Create a function called `sort_unique_chars` that takes a string containing only lowercase alphabets as input and returns a list of unique characters in ascending order. The function should not contain any duplicate elements.
"""

def sort_unique_chars(string):
    """
    Returns a list of unique characters in the input string in ascending order.

    Args:
    string (str): The input string containing only lowercase alphabets.

    Returns:
    list: A list of unique characters in ascending order.
    """
    return sorted(set(string))