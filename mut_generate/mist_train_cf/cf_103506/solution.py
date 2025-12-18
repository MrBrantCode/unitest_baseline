"""
QUESTION:
Write a function `max_subarray_sum(arr)` that takes an array of integers as input and returns the maximum sum of a subarray containing at least two elements. The function should return the maximum sum found in the array.
"""

def max_subarray_sum(arr):
    n = len(arr)
    max_sum = float('-inf')
    current_sum = 0

    for i in range(n):
        current_sum += arr[i]

        if current_sum > max_sum and i > 0:
            max_sum = current_sum
        
        if current_sum < 0:
            current_sum = 0

    return max_sum if max_sum != float('-inf') else 0