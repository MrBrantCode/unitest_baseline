"""
QUESTION:
Write a function called `sort_descending` that takes a list of strings as input and returns the list sorted in descending order.
"""

def sort_descending(lst):
    """
    This function takes a list of strings as input and returns the list sorted in descending order.

    Args:
        lst (list): A list of strings

    Returns:
        list: The input list sorted in descending order
    """
    lst.sort(reverse=True)
    return lst