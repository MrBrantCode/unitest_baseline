"""
QUESTION:
You are given two groups of points where the first group has `size1` points and the second group has `size2` points, with `size1 >= size2`. The cost of connecting any two points is given in a `size1 x size2` matrix where `cost[i][j]` is the cost of connecting point `i` of the first group and point `j` of the second group. Each point in the first group can only be connected to a maximum of two points in the second group and vice versa. Implement a function `connectTwoGroups(cost)` to return the minimum cost it takes to connect the two groups.

Constraints: 
- `size1 == cost.length`
- `size2 == cost[i].length`
- `1 <= size1, size2 <= 12`
- `size1 >= size2`
- `0 <= cost[i][j] <= 100`
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
                if ((s >> j) & 1) == 0: # if point j is not connected yet
                    ns = s | (1 << j) # set the j-th bit to 1
                    # Try to connect point i in group 1 with point j in group 2
                    dp[i + 1][ns] = min(dp[i + 1][ns], dp[i][s] + cost[i][j])
            if i + 1 < size1: # if there's more points in group1
                dp[i + 1][s] = min(dp[i + 1][s], dp[i][s])

    res = min(dp[size1][s] + sum(min_cost2[j] for j in range(size2) if ((s >> j) & 1) == 0) for s in range(1 << size2))
    return res