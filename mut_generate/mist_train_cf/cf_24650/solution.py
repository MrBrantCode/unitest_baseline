"""
QUESTION:
Write a function called `reverse_sort` that takes a list of integers as input and returns the list in reverse sorted order. The input list is guaranteed to contain only unique integers.
"""

def reverse_sort(nums):
    """
    Returns the input list of unique integers in reverse sorted order.
    
    Args:
        nums (list): A list of unique integers.
    
    Returns:
        list: The input list in reverse sorted order.
    """
    return sorted(nums, reverse=True)