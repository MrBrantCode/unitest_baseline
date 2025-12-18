"""
QUESTION:
Write a function `minCost` that takes an array `houses`, a 2D matrix `cost`, and an integer `target` as input and returns the least possible cost to paint all the remaining houses in a manner that results in exactly `target` neighborhoods. If achieving this is impossible, return `-1`. The function should have the following constraints:
- `m == houses.length == cost.length`
- `n == cost[i].length`
- `1 <= m <= 100`
- `1 <= n <= 20`
- `1 <= target <= m`
- `0 <= houses[i] <= n`
- `1 <= cost[i][j] <= 10^4`
"""

def minCost(houses, cost, m, n, target):
    dp = [[[float('inf')] * n for _ in range(target + 1)] for _ in range(m)]

    for k in range(n):
        if houses[0] == 0 or houses[0] == k + 1:
            dp[0][1][k] = cost[0][k]

    for i in range(1, m):
        for j in range(1, min(i + 1, target + 1)):
            for k in range(n):
                if houses[i] == 0 or houses[i] == k + 1:
                    for prev in range(n):
                        if prev != k:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - 1][prev] + cost[i][k])
                        else:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][prev] + cost[i][k])

    ans = min(dp[m - 1][target])
    return ans if ans != float('inf') else -1