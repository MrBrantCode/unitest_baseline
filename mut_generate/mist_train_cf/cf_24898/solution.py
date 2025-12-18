"""
QUESTION:
Create a function named `searchAndReplace` that takes an array of numbers as input, replaces each non-negative number with its square root, and returns the modified array.
"""

import math

def searchAndReplace(nums):
    for i in range(len(nums)):
        if nums[i] >= 0:
            nums[i] = math.sqrt(nums[i])
    return nums