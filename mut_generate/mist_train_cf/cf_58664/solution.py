"""
QUESTION:
Write a function `min_subarray_sum(nums)` that takes a list of integers `nums` as input and returns the smallest possible sum of a contiguous subset within the given list. The function should be able to handle lists of any length and should have a time complexity of O(n).
"""

def min_subarray_sum(nums):
    current_sum = min_sum = nums[0]
    for num in nums[1:]:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    return min_sum