"""
QUESTION:
You are given an array of non-negative integers representing the amount of money of each house arranged in a circle, meaning the first house is adjacent to the last house. You are not allowed to rob adjacent houses. Write a function `rob(nums)` that takes in an array `nums` and returns the maximum amount of money that can be robbed without alerting the police.
"""

def rob(nums):
    def rob_range(start, end):
        max_rob = 0
        prev_rob = 0
        for i in range(start, end):
            prev_rob, max_rob = max_rob, max(max_rob, prev_rob + nums[i])
        return max_rob

    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    return max(rob_range(0, len(nums) - 1), rob_range(1, len(nums)))