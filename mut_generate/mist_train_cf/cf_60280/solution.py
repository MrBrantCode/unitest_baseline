"""
QUESTION:
Write a function `reverse_sort` to sort a given list of integers in descending order. The function should take a list of integers as input and return the sorted list. The list should be sorted in-place, meaning the original list is modified.
"""

def reverse_sort(lst):
    """
    Sorts a given list of integers in descending order.

    Args:
        lst (list): A list of integers.

    Returns:
        list: The sorted list in descending order.
    """
    lst.sort(reverse=True)
    return lst