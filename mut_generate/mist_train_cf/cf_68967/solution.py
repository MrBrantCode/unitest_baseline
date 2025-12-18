"""
QUESTION:
Write a function named `twoSum` that takes an array of integers `nums` and an integer `target` as input and returns the indices of two numbers in `nums` that add up to `target`. You may assume that each input has exactly one solution and that no element can be used twice. The answer can be returned in any order. The length of `nums` is between 2 and 10^3, and the range of `nums[i]` and `target` is between -10^9 and 10^9.
"""

def twoSum(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_map:
            return [hash_map[complement], i]
        else:
            hash_map[nums[i]] = i
    return []