"""
QUESTION:
Write a function `twoSum` that takes an array of integers `nums` and an integer `target` as input and returns the indices of the two numbers in the array such that they add up to the target. The function should assume that each input has exactly one solution, and it should not use the same element twice.
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    foo = {}
    for i, j in enumerate(nums):
        complement = target - j
        if complement in foo:
            return [foo.get(complement), i]
        foo[j] = i