"""
QUESTION:
Write a function `remove_and_sort` that takes a list of integers and an integer `target` as input, removes all occurrences of `target` from the list, and returns the resulting list in ascending order. The function should not modify the original list.
"""

def remove_and_sort(arr, target):
    """
    Removes all occurrences of a target integer from a list and returns the resulting list in ascending order.

    Args:
        arr (list): A list of integers.
        target (int): The target integer to be removed.

    Returns:
        list: The resulting list in ascending order.
    """
    return sorted([x for x in arr if x != target])