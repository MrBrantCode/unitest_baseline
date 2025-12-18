"""
QUESTION:
Create a function named maxSubArraySum that takes an array of integers as input and returns the maximum sum of a contiguous subarray. The function should use Kadane's algorithm to find the maximum sum.
"""

def maxSubArraySum(arr):
    """
    This function returns the maximum sum of a contiguous subarray within a given array of integers.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The maximum sum of a contiguous subarray.
    """
    max_so_far = 0  # Initialize maximum sum so far
    max_ending_here = 0  # Initialize maximum sum of subarray ending at current position

    # Loop through each element in the array
    for num in arr:
        # Update maximum sum of subarray ending at current position
        max_ending_here = max_ending_here + num
        
        # If max_ending_here is negative, reset it to 0
        if max_ending_here < 0:
            max_ending_here = 0
        
        # Update maximum sum so far
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    
    # Return maximum sum so far
    return max_so_far