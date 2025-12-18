"""
QUESTION:
Write a function named `twoSum` that takes two parameters: a list of integers `nums` and an integer `target`. The function should return a list of two integers representing the indices of the two numbers in `nums` that add up to `target`. Assume that each input has exactly one solution and you are not allowed to use the same element twice.
"""

def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i