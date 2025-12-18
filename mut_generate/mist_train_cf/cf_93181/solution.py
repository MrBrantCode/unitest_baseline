"""
QUESTION:
Write a function `twoSum(nums, target)` that takes a list of integers `nums` and an integer `target` as input, and returns a list of two indices corresponding to the two numbers in `nums` that add up to `target`. Assume that each input has exactly one solution and no element can be used twice.
"""

def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i