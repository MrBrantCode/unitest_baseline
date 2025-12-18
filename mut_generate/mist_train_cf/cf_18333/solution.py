"""
QUESTION:
Write a function `max_sum_non_contiguous(arr)` that finds the maximum sum for a non-contiguous subarray of a given array. The array can contain both positive and negative numbers. The function should return the maximum sum of a non-contiguous subarray.
"""

def max_sum_non_contiguous(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return max(arr[0], 0)
    
    incl = max(arr[0], 0)
    excl = 0
    
    for i in range(1, len(arr)):
        new_excl = max(incl, excl)
        incl = excl + max(arr[i], 0)
        excl = new_excl
    
    return max(incl, excl)