"""
QUESTION:
Write a function named `split_string_by_length` that takes a string and an integer greater than the length of the string as input, splits the string into substrings of the given integer length, and returns the substrings in a list sorted in descending order.
"""

def split_string_by_length(input_str, length):
    """
    Splits a string into substrings of a given length and returns them in a list sorted in descending order.

    Args:
        input_str (str): The input string to be split.
        length (int): The length of the substrings.

    Returns:
        list: A list of substrings in descending order.
    """
    return sorted([input_str[i:i+length] for i in range(0, len(input_str), length)], reverse=True)