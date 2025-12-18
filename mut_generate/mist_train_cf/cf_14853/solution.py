"""
QUESTION:
Write a function named `max_pair_sum` that finds the maximum sum of four integers in an array. The function should take an array of integers as input and return the maximum sum of four integers. The array will contain at least four integers. The integers in the array can be positive, negative, or zero.
"""

def max_pair_sum(nums):
    """
    This function finds the maximum sum of four integers in an array.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    int: The maximum sum of four integers in the array.
    """
    
    # Sort the array in descending order
    nums.sort(reverse=True)
    
    # Return the sum of the four largest numbers
    return sum(nums[:4])