"""
QUESTION:
Find the index of the maximum value in a list of integers.

Create a function called `find_max_index` that takes a list of integers as input and returns the index of the maximum value in the list. The function should not take any additional arguments.
"""

def find_max_index(lst):
    """
    Find the index of the maximum value in a list of integers.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The index of the maximum value in the list.
    """
    # Find the highest integer in the list.
    max_value = max(lst)

    # Find the position(index) of this highest integer in the list.
    max_index = lst.index(max_value)

    return max_index