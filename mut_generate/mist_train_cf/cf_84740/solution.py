"""
QUESTION:
Create a function `split_and_sort` that takes two parameters: a string `my_string` and a delimiter `delimiter`. The function should split `my_string` into substrings based on `delimiter`, then return the substrings in alphabetical order. The function should be case-sensitive and consider punctuation as part of the substrings.
"""

def split_and_sort(my_string, delimiter):
    """
    Splits a string into substrings based on a delimiter and returns the substrings in alphabetical order.
    
    Args:
        my_string (str): The input string to be split.
        delimiter (str): The delimiter used to split the string.
    
    Returns:
        list: A list of substrings in alphabetical order.
    """
    return sorted(my_string.split(delimiter))