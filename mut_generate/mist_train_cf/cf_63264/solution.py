"""
QUESTION:
Write a function `connectTwoGroups` that takes a 2D list `cost` where `cost[i][j]` is the cost to connect point `i` in group 1 to point `j` in group 2, and returns the minimum cost to connect all points in group 1 to all points in group 2. The function should use dynamic programming to achieve an efficient solution.
"""

from typing import List
import math

def connectTwoGroups(cost: List[List[int]]) -> int:
    size1, size2 = len(cost), len(cost[0])
    min_cost2 = [min(cost[i][j] for i in range(size1)) for j in range(size2)]
    dp = [[math.inf] * (1 << size2) for _ in range(size1 + 1)]
    dp[0][0] = 0

    for i in range(size1):
        for s in range(1 << size2):
            for j in range(size2):
                if ((s >> j) & 1) == 0: 
                    ns = s | (1 << j) 
                    dp[i + 1][ns] = min(dp[i + 1][ns], dp[i][s] + cost[i][j])
                if i + 1 < size1: 
                    dp[i + 1][s] = min(dp[i + 1][s], dp[i][s])

    res = min(dp[size1][s] + sum(min_cost2[j] for j in range(size2) if ((s >> j) & 1) == 0) for s in range(1 << size2))
    return res