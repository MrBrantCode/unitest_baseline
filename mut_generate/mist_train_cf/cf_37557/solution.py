"""
QUESTION:
Write a function `power_and_multiply` that takes a list of integers as input, raises each integer to the power of 5, multiplies all the results together, and returns the final product. The input list is guaranteed to contain at least one element.
"""

from functools import reduce

def power_and_multiply(nums):
    """
    Raises each integer in the input list to the power of 5 and returns the product of the results.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        int: The product of the powered integers.
    """
    return reduce(lambda x, y: x * y, map(lambda num: num**5, nums), 1)