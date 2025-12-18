"""
QUESTION:
Write a function `max_subarray_sum` that finds the maximum sum of a contiguous subarray within a one-dimensional array of integers. The function should return the maximum sum, and it should run in linear time complexity (O(n)). The function should take an array of integers as input and return an integer.
"""

def max_subarray_sum(nums):
    if not nums:
        return 0

    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        
    return max_sum