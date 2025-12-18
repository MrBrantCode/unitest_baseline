"""
QUESTION:
Find Missing Number in Array

Write a function called `find_missing_number_in_array` that takes a list of integers from 1 to n as input, where one number is missing, and returns the missing number. The function should assume that there is exactly one number missing from the array.
"""

def find_missing_number_in_array(nums):
    """
    This function finds the missing number in a list of integers from 1 to n.
    
    Args:
    nums (list): A list of integers from 1 to n with one number missing.
    
    Returns:
    int: The missing number in the list.
    """
    n = len(nums)
    total = (n + 1) * (n + 2) // 2
    return total - sum(nums)