"""
QUESTION:
Write a function `remove_duplicates_and_sort_desc` that takes an array of integers as input, removes duplicates, and returns the remaining items in descending order.
"""

def remove_duplicates_and_sort_desc(arr):
    """
    Removes duplicates from the input array and returns the remaining items in descending order.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The input list with duplicates removed and sorted in descending order.
    """
    return sorted(set(arr), reverse=True)