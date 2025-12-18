"""
QUESTION:
Write a function named `transform_and_sort` that takes a list of integers as input, squares each number in the list, and returns the squared numbers in descending order.
"""

def transform_and_sort(nums):
    """
    This function takes a list of integers, squares each number, 
    and returns the squared numbers in descending order.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list of squared integers in descending order.
    """
    return sorted([num ** 2 for num in nums], reverse=True)