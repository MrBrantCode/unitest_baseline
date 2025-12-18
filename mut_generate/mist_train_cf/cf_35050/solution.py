"""
QUESTION:
Create a function named `maxProductOfThree` that takes a list of integers as input and returns the maximum product of any three numbers in the list. If the input list contains less than three integers, the function should return 0.
"""

from typing import List

def maxProductOfThree(nums: List[int]) -> int:
    if len(nums) < 3:
        return 0

    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])