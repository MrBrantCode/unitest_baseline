"""
QUESTION:
Given an array of integers, write a function `max_subarray_sum` to find the maximum sum of a contiguous subarray within the array. The function should return the maximum sum and the start and end indices of the subarray. Assume that if the array contains all negative numbers, the function should return the maximum negative number as the sum. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def max_subarray_sum(arr):
    """
    This function finds the maximum sum of a contiguous subarray within the array.
    
    Args:
    arr (list): A list of integers.
    
    Returns:
    tuple: A tuple containing the maximum sum and the start and end indices of the subarray.
    """
    
    # Initialize max_so_far as negative infinity and max_ending_here as 0
    max_so_far = float('-inf')
    max_ending_here = 0
    
    # Initialize start and end indices
    start = 0
    end = 0
    temp_start = 0
    
    # Iterate over the array
    for i in range(len(arr)):
        # Add the current element to max_ending_here
        max_ending_here += arr[i]
        
        # If max_ending_here becomes less than the current element, 
        # assign the value of the current element to max_ending_here
        if max_ending_here < arr[i]:
            max_ending_here = arr[i]
            temp_start = i
        
        # If max_ending_here is greater than max_so_far, 
        # assign the value of max_ending_here to max_so_far
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i
    
    # Return the maximum sum and the start and end indices
    return max_so_far, start, end