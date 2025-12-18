"""
QUESTION:
Implement a function `canAliceWin(nums)` that determines if Alice can win the Advanced Chalkboard Addition Game, given a list of non-negative integers `nums`. In this game, two players take turns erasing a number from the list or replacing an even number with its half, rounded down. The game ends when the sum of the remaining numbers is 0, with the player who made the last move losing. The function should return `True` if Alice can win with optimal strategies and `False` otherwise.

The input list `nums` satisfies the constraints: `1 <= len(nums) <= 1000` and `0 <= nums[i] <= 2^16`.
"""

def canAliceWin(nums):
    MAXN = max(nums)
    fun = [0] * (MAXN + 1)
    for x in range(1, MAXN + 1):
        next_vals = set()
        if x % 2 == 0: 
            next_vals = {fun[0], fun[x // 2]}
        else: 
            next_vals = {fun[0]}
        mex = 0
        while mex in next_vals:
            mex += 1
        fun[x] = mex
    xor_res = 0
    for x in nums:
        xor_res ^= fun[x]
    return xor_res != 0