"""
QUESTION:
You are given a `m x n` grid populated with non-negative integers, where certain cells are designated as obstacles (indicated by -1). The goal is to find a route from the top left to the bottom right that results in the smallest sum of all numbers traversed along this path. Permissible movements are only downwards or to the right at any given moment. Implement a function `minPathSum(grid)` that returns the smallest sum of all numbers traversed along the path. If it's not possible to reach the destination due to obstacles, return -1.

Constraints:
`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 200`
`-1 <= grid[i][j] <= 100`
"""

def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    inf = float('inf')
    dp = [[inf for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][1] = dp[1][0] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if grid[i-1][j-1] == -1:
                continue
            dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])
    
    return dp[-1][-1] if dp[-1][-1] != inf else -1