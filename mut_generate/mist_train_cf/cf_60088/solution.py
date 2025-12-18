"""
QUESTION:
Write a function `minPath(grid, k)` that finds the shortest chain consisting of `k` components within an NxN two-dimensional array `grid`, where `N` is 2 or above and each cell contains a unique value between 1 and `N * N`. The function should return an orderly enumeration of the values constituting this minimal chain, where the chain can start from any single cell and move to adjacent cells linked by a common edge.
"""

def minPath(grid, k):
    N = len(grid)
    visited = [[False]*N for _ in range(N)]
    minpath = [N*N]*k 

    def dfs(i, j, path): 
        if len(path) == k:
            nonlocal minpath
            minpath = min(minpath, path) 
            return
        for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]: 
            if 0 <= x < N and 0 <= y < N and not visited[x][y]: 
                visited[x][y] = True
                dfs(x, y, path+[grid[x][y]]) 
                visited[x][y] = False

    for i in range(N):
        for j in range(N):
            visited[i][j] = True
            dfs(i, j, [grid[i][j]]) 
            visited[i][j] = False

    return minpath