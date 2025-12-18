"""
QUESTION:
Develop a function `minPath` that takes as input a 2D grid and an integer k, and returns the lexicographically smallest path of length k in the grid. The grid is of size N x N (where N >= 2) with unique values ranging from 1 to N*N. The function should be able to start from any cell and move to any neighboring cell, and it should not move out of the grid's boundaries. If two paths have the same length k, the path with the lexicographically smaller sequence of cell values is considered smaller.
"""

def minPath(grid, k):
    n = len(grid)
    result = [float('inf')] * k
    path = [0] * k
    visited = [[False for _ in range(n)] for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(i, j, depth):
        path[depth] = grid[i][j]
        if depth + 1 == k:
            if compare(path, result, k) < 0:
                result[:] = path[:]
            return
        visited[i][j] = True
        for dir in directions:
            ni, nj = i + dir[0], j + dir[1]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                dfs(ni, nj, depth + 1)
        visited[i][j] = False

    def compare(a, b, k):
        for i in range(k):
            if a[i] != b[i]:
                return -1 if a[i] < b[i] else 1
        return 0

    for i in range(n):
        for j in range(n):
            dfs(i, j, 0)
    return result