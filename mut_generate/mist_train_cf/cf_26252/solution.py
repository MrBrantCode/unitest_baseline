"""
QUESTION:
Write a function called `max_integer` that takes a list of integers as input and returns the maximum integer in the list. The function should assume the input list is not empty and only contains integers.
"""

def max_integer(lst):
    """
    Returns the maximum integer in a given list of integers.

    Args:
    lst (list): A list of integers.

    Returns:
    int: The maximum integer in the list.
    """
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val