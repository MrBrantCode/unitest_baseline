"""
QUESTION:
Design a function `maxSumPath(grid, k)` that finds the maximal cumulative value possible from traversing exactly `k` cells of an N x N grid where `N` is at least 2. The function should take two parameters: `grid`, a 2D list of unique integers between 1 and `N*N` (inclusive), and `k`, the number of cells to traverse. The traversal can only occur vertically or horizontally, remaining within grid boundaries, and can start from any cell. The function should return a list of cell values corresponding to the maximum sum path.
"""

def maxSumPath(grid, k):
    n = len(grid)
    directions = [(0,1), (0,-1), (-1,0), (1,0)] # right, left, up, down directions

    def dfs(x, y, k, cur):
        nonlocal maxSum
        nonlocal path
        nonlocal tmpPath
        if x < 0 or y < 0 or x >= n or y >= n or (x, y) in visited or k == 0:
            return
        visited.add((x, y))
        cur.append(grid[x][y])
        if k == 1 and sum(cur) > maxSum:
            maxSum = sum(cur)
            path = cur[:]
        else:
            for dx, dy in directions:
                dfs(x+dx, y+dy, k-1, cur)
        visited.remove((x, y))
        cur.pop()

    maxSum = -1
    path = []
    for i in range(n):
        for j in range(n):
            visited = set()
            tmpPath = []
            dfs(i, j, k, tmpPath)
    return path