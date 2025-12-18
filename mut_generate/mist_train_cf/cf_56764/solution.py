"""
QUESTION:
Write a function named `sort_tuple_reverse` that takes a tuple of strings as input and returns the tuple sorted alphabetically in reverse (Z-A) order.
"""

def sort_tuple_reverse(tup):
    """
    Sorts a tuple of strings in reverse alphabetical order.

    Args:
        tup (tuple): A tuple of strings.

    Returns:
        tuple: The sorted tuple in reverse alphabetical order.
    """
    return tuple(sorted(tup, reverse=True))