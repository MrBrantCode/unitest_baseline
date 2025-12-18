"""
QUESTION:
Write a function `connectTwoGroups` that takes a 2D array `cost` and an integer `k` as input and returns the minimum cost to connect two groups of nodes. The `cost` array represents the cost of connecting each node in the first group to each node in the second group. The function should use dynamic programming and bitmask to find the minimum cost. The function `connectTwoGroups` should call a helper function `dfs` to perform the dynamic programming. The `dfs` function takes seven parameters: `point`, `mask`, `size1`, `size2`, `cost`, `min_cost`, and `dp`, and returns the minimum cost. 

Restrictions: The `cost` array should be a 2D array where each element is a non-negative integer, and `k` should be an integer. The function should use a bitmask to represent subsets of nodes in the second group.
"""

def dfs(point, mask, size1, size2, cost, min_cost, dp):
    if point == -1:
        return sum(i for i in range(size2) if (mask & 1 << i) == 0 for i in min_cost)
    elif dp[point][mask] != float('inf'):
        return dp[point][mask]
    else:
        for i in range(size2):
            dp[point][mask] = min(dp[point][mask], cost[point][i] + dfs(point - 1, mask | 1 << i, size1, size2, cost, min_cost, dp))
    return dp[point][mask]

def connectTwoGroups(cost, k):
    size1, size2 = len(cost), len(cost[0])
    min_cost = [min(cost[j][i] for i in range(size1)) for j in range(size2)]
    dp = [[float('inf')] * (1 << size2) for _ in range(size1)]
    res = dfs(size1 - 1, 0, size1, size2, cost, min_cost, dp)
    return res