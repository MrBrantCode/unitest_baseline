"""
QUESTION:
Given a 3-D grid of size m x n x p, representing a box with n balls, where each cell has a diagonal board that can redirect a ball to the right, left, front, or back. The box is open on the top and bottom sides. The boards are represented as 1 (right), -1 (left), 2 (front), or -2 (back). The task is to write a function `findBall` that takes the grid as input and returns an array of size n where each element represents the column that the ball falls out of at the bottom after dropping the ball from the corresponding column at the top, or -1 if the ball gets stuck in the box.

The constraints are: 
- 1 <= m, n, p <= 100 
- grid[i][j][k] is 1, -1, 2, or -2.
"""

def findBall(grid):
    m, n, p = len(grid), len(grid[0]), len(grid[0][0])

    directions = [(0, 1, 0), (0, -1, 0), (-1, 0, 0), (1, 0, 0)]

    def is_valid(x, y, z):
        return 0 <= x < m and 0 <= y < n and 0 <= z < p

    def dfs(x, y, z, visited):
        if not is_valid(x, y, z) or visited[x][y][z]:
            return -1
        if x == m - 1:
            return y
        visited[x][y][z] = True
        dx, dy, dz = directions[grid[x][y][z]//abs(grid[x][y][z]) if grid[x][y][z] in [-2, 2] else (grid[x][y][z] + 1)]
        nx, ny, nz = x + dx, y + dy, z + dz
        return dfs(nx, ny, nz, visited)

    visited = [[[False]*p for _ in range(n)] for _ in range(m)]
    res = [dfs(0, i, 0, visited) for i in range(n)]
    return res