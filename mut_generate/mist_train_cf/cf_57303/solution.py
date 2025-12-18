"""
QUESTION:
Write a function `transform_string_to_int` that takes a list of string type elements as input and returns a new list with the same elements converted to integer type. The input list may contain only string representations of integers.
"""

def transform_string_to_int(strings):
    """
    Converts a list of string representations of integers into a list of integers.

    Args:
        strings (list[str]): A list of string type elements.

    Returns:
        list[int]: A new list with the same elements converted to integer type.
    """
    return [int(i) for i in strings]