"""
QUESTION:
Write a function `max_quotient` that takes a list of distinct integers as input and returns the maximum quotient achievable via the division of two distinct integers from the list. The input list may contain both positive and negative numbers, but not zero.
"""

def max_quotient(nums):
    """
    This function calculates the maximum quotient achievable via the division of two distinct integers from the list.
    
    Args:
        nums (list): A list of distinct integers.
    
    Returns:
        float: The maximum quotient achievable via the division of two distinct integers from the list.
    """
    nums.sort()
    return nums[-1] / nums[0]