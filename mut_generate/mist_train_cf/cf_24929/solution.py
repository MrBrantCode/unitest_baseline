"""
QUESTION:
Write a function `max_subarray_sum` that takes an array of integers as input and returns the maximum sum of any subarray. The function should return 0 if the input array is empty or contains all negative numbers with no positive sum.
"""

def max_subarray_sum(nums):
    """
    Returns the maximum sum of any subarray of the given array of integers.
    If the input array is empty or contains all negative numbers with no positive sum, returns 0.
    
    Parameters:
    nums (list): A list of integers.
    
    Returns:
    int: The maximum sum of any subarray.
    """
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum if max_sum > 0 else 0