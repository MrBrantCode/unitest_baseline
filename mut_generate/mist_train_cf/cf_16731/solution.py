"""
QUESTION:
Write a function named `max_sum_subarray` that takes an array of integers as input and returns the maximum sum of all possible subarrays. The function should handle both positive and negative numbers in the array and have a time complexity of O(n^2).
"""

def max_sum_subarray(arr):
    """
    Returns the maximum sum of all possible subarrays.

    Args:
        arr (list): An array of integers.

    Returns:
        int: The maximum sum of all possible subarrays.
    """
    max_sum = float('-inf')
    
    for i in range(len(arr)):
        curr_sum = 0
        
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            
            if curr_sum > max_sum:
                max_sum = curr_sum
    
    return max_sum