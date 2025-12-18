"""
QUESTION:
Write a function `max_subarray_sum` that takes an array of integers as input and returns the maximum sum of any contiguous subarray. The subarray should contain at least one integer. If all numbers in the array are negative, return the maximum number in the array.
"""

def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    
    return max_sum