"""
QUESTION:
Write a function `max_subarray_sum` that takes a list of integers as input and returns the maximum sum of any contiguous subarray in the list. The time complexity of the function should be O(n), where n is the length of the list, and the space complexity should be O(1). The function should handle the case when all elements in the list are negative and return the maximum negative element as the maximum sum.
"""

def max_subarray_sum(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum