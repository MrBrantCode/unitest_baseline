"""
QUESTION:
Write a function `max_subarray_sum` that takes a list of integers as input and returns the maximum sum of a contiguous subarray. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def max_subarray_sum(arr):
    if len(arr) == 0: return 0
    
    curr_max = global_max = arr[0]
    
    for num in arr[1:]:
        curr_max = max(num, curr_max + num)
        global_max = max(global_max, curr_max)
     
    return global_max