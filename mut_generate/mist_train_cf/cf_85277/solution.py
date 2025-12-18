"""
QUESTION:
Given an array of non-negative integers `nums` representing the maximum jump length at each position, write a function `jump(nums)` that returns the minimum number of jumps required to reach the last index. Assume that you can always reach the last index, and the input array length is between 1 and 1000 (inclusive) with each element between 0 and 10^5 (inclusive).
"""

def entance(nums):
    jumps = 0
    end = 0
    furthestReach = 0
    for i in range(len(nums) - 1):
        furthestReach = max(furthestReach, nums[i] + i)
        if i == end:
            jumps += 1
            end = furthestReach
    return jumps