"""
QUESTION:
Write a Python function `is_valid` that takes an input list of integers `nums` and returns a boolean value indicating whether the list can be rearranged into a valid sequence where each pair of adjacent elements has a difference of either 1 or -1.

Note: The function should not return the rearranged sequence, but only a boolean value indicating whether such a rearrangement is possible.
"""

def is_valid(nums):
    if len(nums) % 2 != 0:
        return False
    nums.sort()
    for i in range(0, len(nums), 2):
        if abs(nums[i] - nums[i + 1]) != 1:
            return False
    return True