"""
QUESTION:
Create a function named `reverse_list` that takes a list as input and returns the same list with its elements in reverse order using recursion. The function should not modify the original list and should handle lists of any length.
"""

def reverse_list(lst):
    """
    Reverses the order of elements in a list using recursion.

    Args:
        lst (list): The input list.

    Returns:
        list: A new list with the elements in reverse order.
    """
    if len(lst) <= 1:
        return lst
    else:
        return reverse_list(lst[1:]) + [lst[0]]