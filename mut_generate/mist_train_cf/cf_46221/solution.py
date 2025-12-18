"""
QUESTION:
Given an array `nums` of `n` integers, where `n` is between 1 and 10^4 inclusive and each element `nums[i]` is between -10^9 and 10^9 inclusive, write a function `minSteps(nums)` that returns the least number of steps needed to make all elements in the array identical. In each step, `n - 1` elements of the array can be incremented by 1.
"""

def minSteps(nums):
    return sum(nums) - min(nums)*len(nums)