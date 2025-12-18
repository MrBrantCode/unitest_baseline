"""
QUESTION:
Write a function named `find_max_difference` that takes an array of integers as input and returns the maximum difference between any two consecutive elements in the array.
"""

def entrance(nums):
    max_diff = float('-inf')
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i-1]
        if diff > max_diff:
            max_diff = diff
    return max_diff