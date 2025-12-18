"""
QUESTION:
Write a function `maxSubarraySum` that takes an array of integers as input and returns the maximum sum of a subarray within the given array. The function should return 0 if the maximum sum is negative.
"""

def maxSubarraySum(arr):
    """
    This function calculates the maximum sum of a subarray within the given array.
    If the maximum sum is negative, it returns 0.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The maximum sum of a subarray.
    """
    max_sum = 0
    current_sum = 0

    for num in arr:
        current_sum += num
        
        if current_sum < 0:
            current_sum = 0
            
        max_sum = max(current_sum, max_sum)
    
    return max_sum if max_sum > 0 else 0