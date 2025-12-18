"""
QUESTION:
Create a function `minPath(grid, k)` that finds the least valued path containing exactly k elements without repetition from an NxN grid, starting from any cell. The function should not exceed grid borders, include diagonally adjacent cells, and return a sorted list of unique values along the path. The input grid is a 2D list of integers with N >= 2, and k is a positive integer.
"""

from heapq import *
import sys
directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

def minPath(grid, k):
    n = len(grid)
    visited = set()
    ans = sys.maxsize
    path = []

    def dfs(i, j, k, s):
        nonlocal ans, path
        if (i, j) in visited or not (0 <= i < n) or not (0 <= j < n) or grid[i][j] >= ans:
            return
        visited.add((i, j))
        heappush(s, -grid[i][j])
        if len(s) > k:
            heappop(s)
        if len(s) == k:
            ans = min(ans, -s[0])
            path = sorted([-x for x in s])
        for d in directions:
            dfs(i + d[0], j + d[1], k, s)
        visited.remove((i, j))
        heappop(s)

    for i in range(n):
        for j in range(n):
            dfs(i, j, k, [])
    return path