"""
QUESTION:
Design a function called maxSubArraySum that takes an array of integers and its size as input, and returns the maximum sum of a contiguous subarray within the given array. The function should be able to handle arrays containing both positive and negative numbers.
"""

def maxSubArraySum(arr, n):
    """
    This function returns the maximum sum of a contiguous subarray within the given array.
    
    Parameters:
    arr (list): The input array of integers.
    n (int): The size of the input array.
    
    Returns:
    int: The maximum sum of a contiguous subarray.
    """
    max_ending_here = arr[0]
    max_ending_so_far = arr[0]
    
    for i in range(1, n):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_ending_so_far = max(max_ending_so_far, max_ending_here)
    
    return max_ending_so_far