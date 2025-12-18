"""
QUESTION:
Create a function `convert_string_to_2d_array` that takes a string as input and returns a 2D array of words, where each word is represented as an array of its individual characters. Ensure that the first character of each word in the output array is in uppercase, and the rest are in lowercase. Discard words that have less than 3 characters in them.
"""

def convert_string_to_2d_array(s):
    """
    Convert a string into a 2D array of words, where each word is an array of its individual characters.
    The first character of each word is in uppercase, and the rest are in lowercase.
    Discard words that have less than 3 characters.

    Args:
        s (str): The input string.

    Returns:
        list: A 2D array of words, where each word is an array of its individual characters.
    """
    words = [word for word in s.split() if len(word) >= 3]
    words = [word.capitalize() for word in words]
    return [list(word) for word in words]