"""
QUESTION:
Write a function named `maxSumPath` that takes two parameters: `grid` and `k`. The `grid` is an NxN grid where N is at least 2, and each cell contains a unique value from 1 to N*N. The `k` is the number of cells to select. The function should return the highest possible sum of exactly `k` cells that can be obtained by starting at any cell and moving to adjacent cells that share an edge within the grid boundaries.
"""

def maxSumPath(grid, k):
    n = len(grid)
    visited = set()
    max_sum = [0]
    
    def dfs(x, y, k, cur_sum):
        if k == 0:
            max_sum[0] = max(max_sum[0], cur_sum)
            return
        
        visited.add((x, y))
        
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                dfs(nx, ny, k - 1, cur_sum + grid[nx][ny])
                
        visited.remove((x, y))
    
    for i in range(n):
        for j in range(n):
            dfs(i, j, k - 1, grid[i][j])
    
    return max_sum[0]