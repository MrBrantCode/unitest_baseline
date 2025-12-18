"""
QUESTION:
Write a function `calculate_lcm(nums)` that calculates the Least Common Multiple (LCM) of a dynamic array of numbers. The function should take an array of integers as input and return their LCM. The solution should be optimized for both time and memory complexity, with a time complexity of O(n) and a space complexity of O(1), where n is the length of the input array.
"""

import math

def calculate_lcm(nums):
    lcm = nums[0]
    for i in range(1, len(nums)):
        lcm = lcm * nums[i]//math.gcd(lcm, nums[i])
    return lcm