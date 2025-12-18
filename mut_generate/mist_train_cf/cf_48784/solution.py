"""
QUESTION:
Write a function `minPath` that takes a 2D grid of prime numbers and an integer `k` as input, and returns the shortest sequence of `k` prime numbers that can be formed by traversing the grid in an anti-clockwise direction from any starting cell. The grid is an NxN matrix, where 4 ≤ N ≤ 10, and each cell contains a prime number between 2 and N^2. The function should return the sequence in sorted order.
"""

def minPath(grid, k):
    n = len(grid)
    dx = [0, 1, 0, -1] 
    dy = [-1, 0, 1, 0] 
    visited = [[False]*n for _ in range(n)]
    min_path = [float('inf')]*k
    path = []

    def is_valid(x, y):
        return 0<=x<n and 0<=y<n and not visited[x][y]

    def dfs(x, y, k):
        nonlocal min_path, path
        if k == 0:
            min_path = min(min_path, sorted(path))
            return
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if is_valid(nx, ny):
                visited[nx][ny] = True
                path.append(grid[nx][ny])
                dfs(nx, ny, k-1)
                visited[nx][ny] = False
                path.pop()

    for i in range(n):
        for j in range(n):
            visited[i][j] = True
            path.append(grid[i][j])
            dfs(i, j, k-1)
            path.pop()
            visited[i][j] = False
    return min_path