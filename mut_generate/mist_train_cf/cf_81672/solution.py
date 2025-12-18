"""
QUESTION:
Write a function called `max_sum_subarray` that takes an integer array as input and returns the maximum sum of a contiguous subarray. The function should be able to handle arrays containing both positive and negative integers.
"""

def max_sum_subarray(array):
    current_max = 0
    global_max = 0
    
    for i in range(0, len(array)):
        current_max = max(array[i], current_max + array[i])
        global_max = max(global_max, current_max)
        
    return global_max