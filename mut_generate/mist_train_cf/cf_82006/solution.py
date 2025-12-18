"""
QUESTION:
Write a Python function `get_unique_chars` that takes a string input from the user and returns a list of unique characters (characters that occur only once) in the string. The function should consider space and case sensitivity.
"""

from collections import Counter

def get_unique_chars(input_string):
    """
    Returns a list of unique characters (characters that occur only once) in the input string.
    The function considers space and case sensitivity.

    Args:
        input_string (str): The input string.

    Returns:
        list: A list of unique characters.
    """
    char_count = Counter(input_string)
    unique_chars = [char for char, count in char_count.items() if count == 1]
    return unique_chars