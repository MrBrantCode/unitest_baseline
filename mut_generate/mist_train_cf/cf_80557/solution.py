"""
QUESTION:
Write a function `jump_game(nums)` that determines the minimum number of jumps to reach the last index in an array `nums`, where each element represents the maximum jump length at that position. If it is impossible to reach the last index, return -1. The function must handle arrays of length between 1 and 3 * 10^4, inclusive, and jump lengths between 0 and 10^5, inclusive.
"""

def canJump(nums):
    if not nums or len(nums) == 1:
        return 0

    jumps = [float('inf')] * len(nums)
    jumps[0] = 0

    for i in range(1, len(nums)):
        for j in range(i):
            if i <= j + nums[j]:
                jumps[i] = min(jumps[i], jumps[j] + 1)

    return jumps[-1] if jumps[-1] != float('inf') else -1