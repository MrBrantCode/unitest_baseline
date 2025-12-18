"""
QUESTION:
Implement the Travelling Salesman Problem using memoization and dynamic programming. 

Create a function named `TSP` that takes a 2D list `graph` and a starting city index `s` as input, where `graph[i][j]` represents the distance from city `i` to city `j`. The function should return the minimum weight of the Hamiltonian cycle (the shortest possible route that visits each city once and returns to the original city).

Restrictions: The function should use memoization to store the results of subproblems and avoid repeat calculations, and its time complexity should be optimized from O(n!) to O(n^2 * 2^n).
"""

from sys import maxsize
from functools import lru_cache

def TSP(graph, s):
    n = len(graph)
    @lru_cache(None)
    def dp(mask, pos):
        if mask == 0:
            return graph[pos][s]
        ans = maxsize
        for city in range(n):
            if ((mask >> city) & 1) == 0:
                continue
            new_mask = mask ^ (1 << city)
            ans = min(ans, graph[pos][city] + dp(new_mask, city))
        return ans
    ans = maxsize
    for city in range(1, n):
        ans = min(ans, graph[s][city] + dp((1 << n) - 1 - (1 << s) - (1 << city), city))
    return ans