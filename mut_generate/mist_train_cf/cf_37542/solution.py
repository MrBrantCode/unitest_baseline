"""
QUESTION:
You are given a list of non-negative integers representing the amount of money of each house arranged in a circle. The goal is to determine the maximum amount of money that can be robbed without alerting the police, with the restriction that you cannot rob adjacent houses.

Write a function `maxRobbery(nums)` to calculate the maximum amount of money that can be robbed. The function takes a list of non-negative integers `nums` where 1 <= len(nums) <= 100 and 0 <= nums[i] <= 1000 as input and returns the maximum amount of money that can be robbed without alerting the police.
"""

from typing import List

def maxRobbery(nums: List[int]) -> int:
    def rob(nums: List[int], start: int, end: int) -> int:
        if start == end:
            return nums[start]
        prev, curr = 0, 0
        for i in range(start, end):
            prev, curr = curr, max(curr, prev + nums[i])
        return curr

    if len(nums) == 1:
        return nums[0]
    return max(rob(nums, 0, len(nums) - 2), rob(nums, 1, len(nums) - 1))