"""
QUESTION:
Write a function `sort_and_remove_duplicates` that takes a list of integers as input, removes any duplicate values, and returns the sorted list in descending order.
"""

def sort_and_remove_duplicates(nums):
    """
    This function takes a list of integers, removes duplicates, and returns the sorted list in descending order.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A sorted list of unique integers in descending order.
    """
    return sorted(set(nums), reverse=True)