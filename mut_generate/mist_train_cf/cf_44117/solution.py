"""
QUESTION:
The function `tree_distance(n, edges)` takes as input an integer `n` and a 2D array `edges` of size `n-1`, where `edges[i] = [ui, vi]` represents a two-way connection between metropolises `ui` and `vi`. The function should return an array of size `n-1` where the `dth` element (1-indexed) represents the number of subtrees where the maximum distance between any two metropolises equals `d`. The constraints are `2 <= n <= 15`, `edges.length == n-1`, `edges[i].length == 2`, and `1 <= ui, vi <= n`, with all pairs `(ui, vi)` being unique.
"""

from collections import defaultdict

def tree_distance(n, edges):
    G = defaultdict(list)
    for u, v in edges:
        G[u-1].append(v-1)
        G[v-1].append(u-1)

    dp = [[0]* (1<<n) for _ in range(n)]
    for mask in range(1, 1<<n):
        for u in range(n):
            if((mask>>u)&1):
                for v in G[u]:
                    if((mask>>v)&1):
                        dp[u][mask] = max(dp[u][mask], dp[v][mask^(1<<u)]+1)

    cnt = [0]*n
    for mask in range(1,1<<n):
        d = max(dp[u][mask] for u in range(n))
        cnt[d] += 1
    return cnt[1:]