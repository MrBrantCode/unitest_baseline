"""
QUESTION:
Write a function `max_sum_subarray(arr)` that takes an array of integers as input and returns the maximum sum of all possible subarrays. The array may contain both positive and negative numbers. The function should handle cases where all numbers in the array are negative.
"""

def max_sum_subarray(arr):
    max_sum = float('-inf')
    curr_sum = 0
    
    for num in arr:
        curr_sum += num
        
        if curr_sum > max_sum:
            max_sum = curr_sum
        
        if curr_sum < 0:
            curr_sum = 0
    
    return max_sum