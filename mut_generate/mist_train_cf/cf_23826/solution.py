"""
QUESTION:
Write a function `max_subarray_sum` that takes an array of integers as input and returns the maximum contiguous subarray sum. The function should have a time complexity of O(n), where n is the number of elements in the array, and should be able to handle arrays containing both positive and negative integers.
"""

def max_subarray_sum(arr): 
    max_so_far = 0 
    max_ending_here = 0

    for i in range(len(arr)): 
        max_ending_here += arr[i] 

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here 

        if max_ending_here < 0: 
            max_ending_here = 0 
    
    return max_so_far