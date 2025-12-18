"""
QUESTION:
You are given an `n x m` grid representing a field of cherries, where each cell is one of three possible integers: `0` (empty), `1` (contains a cherry), or `-1` (contains a thorn that blocks your way). You are also given a list of `k` positions that will become thorns at a certain time. Write a function `cherryPickup(grid, thorns)` to return the maximum number of cherries you can collect by following the rules below:

* Start at position `(0, 0)` and reach `(n - 1, m - 1)` by moving right or down through valid path cells (cells with value `0` or `1`).
* After reaching `(n - 1, m - 1)`, return to `(0, 0)` by moving left or up through valid path cells.
* When passing through a path cell containing a cherry, pick it up, and the cell becomes an empty cell `0`.
* If there is no valid path between `(0, 0)` and `(n - 1, m - 1)`, return `0`.

Constraints:
- `n == grid.length`
- `m == grid[i].length`
- `1 <= n, m <= 50`
- `grid[i][j]` is `-1`, `0`, or `1`
- `grid[0][0] != -1`
- `grid[n - 1][m - 1] != -1`
- `0 <= k <= n*m`
- `thorns[i]` is a valid position in the grid
"""

def cherryPickup(grid, thorns):
    n,m = len(grid), len(grid[0])
    directions = [(1,0), (0,1)]
    dp = [[-9999999]*m for _ in range(n)]
    dp1 = [[-9999999]*m for _ in range(n)]
    thorns = dict(thorns)
    
    def dfs(x, y, dp, visited):
        if (x,y) == (n-1, m-1):
            return grid[x][y]
        if dp[x][y] != -9999999:
            return dp[x][y]
        visited.add((x,y))
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if nx<n and ny<m and grid[nx][ny] != -1 and (nx,ny) not in visited:
                dp[x][y] = max(dp[x][y], dfs(nx, ny, dp, visited)+grid[x][y])
        visited.remove((x,y))
        return dp[x][y]  
        
    cherries = dfs(0, 0, dp, set([(0,0)]))
    grid[0][0] = 0    
    if (n-1,m-1) in thorns:
        grid[thorns[(n-1,m-1)][0]][thorns[(n-1,m-1)][1]] = -1
        del thorns[(n-1,m-1)]
    cherries += dfs(n-1, m-1, dp1, set([(n-1,m-1)]))
    return cherries if cherries>=1 else 0