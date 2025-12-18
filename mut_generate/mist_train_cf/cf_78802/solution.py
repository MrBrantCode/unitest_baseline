"""
QUESTION:
Given an integer `n` and a 2D array `highways` where `highways[i] = [ai, bi]` represents a two-way highway between metropolises `ai` and `bi`, return the supreme network rank of the infrastructure, which is the highest network rank among all pairs of distinct metropolises. The network rank of two distinct metropolises is the cumulative count of highways directly linked to either metropolis, counting a highway that is directly linked to both metropolises only once. 

Constraints: `2 <= n <= 100`, `0 <= highways.length <= n * (n - 1) / 2`, `highways[i].length == 2`, `0 <= ai, bi <= n-1`, `ai != bi`, and each pair of metropolises has at most one highway connecting them.
"""

def supremeNetworkRank(n, highways):
    count = [0]*n
    direct_link = [[False]*n for _ in range(n)]
    res = 0
    for i, j in highways:
        count[i] += 1
        count[j] += 1
        direct_link[i][j] = direct_link[j][i] = True
    for i in range(n):
        for j in range(i+1, n):
            res = max(res, count[i] + count[j] - (1 if direct_link[i][j] else 0))
    return res