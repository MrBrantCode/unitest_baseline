"""
QUESTION:
Implement the function `compute_sum()` that takes an array of integers as input and returns their sum. The array can contain up to 10^6 elements, including positive, negative, and duplicate integers. The function should handle edge cases such as empty arrays, arrays with one element, and arrays with large numbers without exceeding integer data type limits.
"""

def compute_sum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return sum(arr)