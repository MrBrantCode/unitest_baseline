"""
QUESTION:
Write a function named `sort_descending` that takes a list of integers as input. The function should sort the list in descending order and return the sorted list. The list can contain duplicate elements and negative numbers, and all elements including duplicates should be included in the final sorted list. If there are multiple occurrences of an element, they should be grouped together in the sorted list.
"""

def sort_descending(nums):
    """
    Sorts a list of integers in descending order.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The sorted list of integers in descending order.
    """
    return sorted(nums, reverse=True)