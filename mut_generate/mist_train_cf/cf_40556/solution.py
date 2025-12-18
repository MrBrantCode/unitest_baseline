"""
QUESTION:
Implement a function `countWays` that takes a list of integers `nums` and a target sum `target` as input and returns the number of ways to reach the target sum using the elements of `nums`. The function should return the count modulo 10^9 + 7. The count includes all combinations of elements that sum up to the target, where each element can be used at most once.
"""

from typing import List

def countWays(nums: List[int], target: int) -> int:
    mod = 10**9 + 7
    n = len(nums)
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(target + 1):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod
            if j + nums[i] <= target:
                dp[i+1][j + nums[i]] += dp[i][j]
                dp[i+1][j + nums[i]] %= mod

    return dp[n][target]