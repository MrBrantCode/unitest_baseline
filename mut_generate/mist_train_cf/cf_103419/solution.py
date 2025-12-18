"""
QUESTION:
Write a function `remove_duplicates_and_sort` that takes a list of integers as input, removes duplicates, and returns the list in ascending order. The input list may contain negative numbers and/or zero.
"""

def remove_duplicates_and_sort(nums):
    """
    Removes duplicates from a list of integers and returns the list in ascending order.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: The input list with duplicates removed, in ascending order.
    """
    return sorted(list(set(nums)))