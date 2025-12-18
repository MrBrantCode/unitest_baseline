"""
QUESTION:
You are given an array of integers `cost` where `cost[i]` represents the expense of the `ith` step on a staircase. You can ascend one or two steps. You can start from the step at index `0` or `1`. Determine the least expensive path to reach the top of the staircase. The function should be named `minCostClimbingStairs`. The constraints are `2 <= cost.length <= 1000` and `0 <= cost[i] <= 999`.
"""

def minCostClimbingStairs(cost):
    dp = [0] * len(cost)
    dp[0], dp[1] = cost[0], cost[1]
    for i in range(2, len(cost)):
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    return min(dp[-1], dp[-2])