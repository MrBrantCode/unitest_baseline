"""
QUESTION:
Write a function `minCostClimbingStairs` that takes an array `cost` where `cost[i]` represents the cost of reaching the `i-th` step, and returns the minimum cost to reach the top of the staircase. The array `cost` will have at least two elements and at most 1000 elements, and each element will be an integer between 0 and 999.
"""

from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

    return min(dp[n-1], dp[n-2])