"""
QUESTION:
Write a function `countNetworkRank(n, highways)` that takes the number of metropolises `n` and a 2D array `highways` where each `highways[i] = [ai, bi]` represents a two-way highway between metropolises `ai` and `bi`, and returns the supreme network rank of the entire infrastructure, which is the maximum network rank among all pairs of distinct metropolises. The network rank of two distinct metropolises is the total number of highways directly connected to either of the metropolises. 

Constraints: `2 <= n <= 100`, `0 <= highways.length <= n * (n - 1) / 2`, `highways[i].length == 2`, `0 <= ai, bi <= n-1`, `ai != bi`, and each pair of metropolises has at most one highway connecting them.
"""

def countNetworkRank(n, highways):
    count = [0] * n
    
    for a, b in highways:
        count[a] += 1
        count[b] += 1
    
    maxRank = 0
    for i in range(n):
        for j in range(i + 1, n):
            rank = count[i] + count[j] - (i != j and (count[i] > 0 or count[j] > 0) and any(x == i and y == j or x == j and y == i for x, y in highways))
            maxRank = max(maxRank, rank)
    return maxRank