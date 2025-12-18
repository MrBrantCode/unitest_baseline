"""
QUESTION:
You are given an array `nums` of length `n`, where `1 <= n <= 10^5` and `1 <= nums[i] <= 10^9`. Implement a function `isSuitable(nums)` that returns `True` if there exists a subset of `nums` and an integer multiplier for each element in the subset such that their sum equals `1`, and `False` otherwise.
"""

from math import gcd

def isSuitable(nums):
    current_gcd = nums[0]
    for i in range(1, len(nums)):
        current_gcd = gcd(current_gcd, nums[i])
    return current_gcd == 1