"""
QUESTION:
Write an optimized version of the `max_subarray_sum` function that takes in a list of integers and returns the maximum sum of a contiguous subarray within the input list. The function should achieve a time complexity of O(n), where n is the length of the input list. The input list `nums` may contain negative integers, and the function should handle this scenario correctly.
"""

def max_subarray_sum(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum