"""
QUESTION:
You are given an `n x k` cost matrix `costs` representing the cost of painting each of `n` houses with one of `k` colors and an integer `m` representing the maximum number of consecutive houses that can be painted with the same color. Return the minimum cost to paint all houses such that no two adjacent houses have the same color and the same color is not used more than `m` times consecutively. 

Constraints:
- `1 <= n <= 100`
- `1 <= k <= 20`
- `1 <= m <= n`
- `1 <= costs[i][j] <= 20`
"""

def entrance(costs, m):
    n, k = len(costs), len(costs[0])
    dp = [[[float('inf')]*m for _ in range(k)] for _ in range(n)]

    # initialization
    for j in range(k):
        dp[0][j][0] = costs[0][j]

    for i in range(1, n):
        minPrevCost = min(min(dp[i-1][j]) for j in range(k))
        for j in range(k):
            for t in range(1, m):
                if dp[i-1][j][t-1] != float('inf'):
                    dp[i][j][t] = dp[i-1][j][t-1] + costs[i][j]
            dp[i][j][0] = minPrevCost + costs[i][j]

    return min(min(dp[n-1][j]) for j in range(k))