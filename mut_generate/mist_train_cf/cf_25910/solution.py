"""
QUESTION:
Write a function named `maxSubArraySum` that takes an array of integers as input and returns the maximum sum of any contiguous subarray.
"""

def maxSubArraySum(arr):
    """
    This function calculates the maximum sum of any contiguous subarray.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The maximum sum of any contiguous subarray.
    """
    max_so_far = 0
    max_ending_here = 0
    
    for i in arr:
        max_ending_here += i
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
    
    return max_so_far