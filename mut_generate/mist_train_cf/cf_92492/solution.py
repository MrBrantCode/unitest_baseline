"""
QUESTION:
Write a function named `max_subarray_sum` that takes an array of integers as input and returns the maximum sum of a subarray containing at least two elements. The function should not use any external libraries or data structures.
"""

def max_subarray_sum(arr):
    n = len(arr)
    max_sum = float('-inf')
    current_sum = 0

    for i in range(n):
        current_sum += arr[i]

        if current_sum > max_sum and len([x for x in arr if x <= current_sum]) >= 2:
            max_sum = current_sum
        
        if current_sum < 0:
            current_sum = 0

    return max_sum