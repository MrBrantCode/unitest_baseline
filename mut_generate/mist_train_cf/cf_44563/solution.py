"""
QUESTION:
Given a list of integers `nums`, return the index of the dominant element if it is at least double the value of every other number in the array; otherwise, return -1. The dominant element is the maximum value in the array. The length of `nums` is within the range `[1, 50]`, and each `nums[i]` is an integer within the range `[0, 99]`. Implement the function `dominantIndex(nums)`.
"""

def dominantIndex(nums):
    if len(nums) == 1: 
        return 0
    max_val = max(nums)
    max_idx = nums.index(max_val)
    second_max_val = max(num for num in nums if num != max_val)
    return max_idx if max_val >= 2 * second_max_val else -1