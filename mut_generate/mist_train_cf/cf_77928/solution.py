"""
QUESTION:
You are given a 2D cost matrix `costs` representing the cost of painting each house with a certain color. The matrix has `n` rows and `k` columns, where `n` is the number of houses and `k` is the number of colors. Each cell `costs[i][j]` represents the cost of painting house `i` with color `j`. Write a function `minCostII` to return the minimum cost to paint all houses such that no two adjacent houses have the same color. The function should take `costs` as input and return an integer.

Constraints: `1 <= n <= 100`, `1 <= k <= 100`, `1 <= costs[i][j] <= 1000`.
"""

def minCostII(costs):
    if not costs: return 0
    n, k = len(costs), len(costs[0])
    dp = [[0] * k for _ in range(n)]
    dp[0] = costs[0]
    for i in range(1, n):
        min1 = min(dp[i-1])
        idx = dp[i-1].index(min1)
        min2 = min(dp[i-1][:idx]+dp[i-1][idx+1:])
        for j in range(k):
            if j == idx:
                dp[i][j] = min2 + costs[i][j]
            else:
                dp[i][j] = min1 + costs[i][j]
    return min(dp[-1])