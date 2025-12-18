"""
QUESTION:
Create a function `max_min_product` that takes a list of integers as input and returns the product of the maximum and minimum integers in the list. The list will contain at least two integers.
"""

def max_min_product(nums):
    """
    Calculate the product of the maximum and minimum integers in a list.

    Args:
    nums (list): A list of integers.

    Returns:
    int: The product of the maximum and minimum integers in the list.
    """
    return max(nums) * min(nums)