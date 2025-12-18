"""
QUESTION:
You are given an integer array `nums` representing the monetary value in each house arranged linearly, where you cannot rob two contiguous houses on the same night and the houses at the ends of the street are interconnected. Your task is to determine the highest possible sum of money you can pilfer tonight without setting off the police alarm.

The function `rob(nums)` should take an array of integers `nums` as input and return the maximum sum of money that can be stolen. The constraints are `3 <= len(nums) <= 100` and `0 <= nums[i] <= 400`.
"""

def houseRobberII(nums):
    def robRange(start, end):
        rob, no_rob = 0, 0
        for i in range(start, end):
            rob, no_rob = no_rob + nums[i], max(rob, no_rob)
        return max(rob, no_rob)

    return max(robRange(0, len(nums) - 1), robRange(1, len(nums)))