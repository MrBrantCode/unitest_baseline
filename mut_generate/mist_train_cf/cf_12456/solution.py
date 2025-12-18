"""
QUESTION:
Write a function `max_subarray_sum(nums)` that finds the maximum possible sum of a subarray within the given array `nums`. The subarray must contain at least two elements and the elements must be consecutive.
"""

def max_subarray_sum(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum