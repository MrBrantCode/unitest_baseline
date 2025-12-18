"""
QUESTION:
Write a function named `two_sum` that takes an array of integers and an integer target as input and returns two numbers such that they add up to the target. You may assume that each input would have exactly one solution.
"""

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i