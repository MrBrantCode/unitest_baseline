"""
QUESTION:
Write a function `remove_empty_strings` that takes a list of strings as input and returns a new list with all empty strings removed, preserving the original order of the non-empty strings.
"""

def remove_empty_strings(lst):
    """
    This function takes a list of strings as input, removes all empty strings, 
    and returns a new list with the non-empty strings in their original order.

    Args:
        lst (list): A list of strings.

    Returns:
        list: A new list with all empty strings removed.
    """
    return [element for element in lst if element != ""]