"""
QUESTION:
Implement a `search` method in the `Cursor` class that takes a target value and a 2D grid as input and returns the minimum number of steps to reach the target value from the starting position (0, 0) in the grid. The cursor can move in four directions (up, down, left, right) within the grid's bounds. The grid is a square with dimensions n x n, where 1 <= n <= 100, and the values in the grid are integers in the range [-1000, 1000]. If the target value is not found, return -1.
"""

def search(grid, target):
    n = len(grid)
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = [(0, 0, 0)]  # (x, y, steps)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    while queue:
        x, y, steps = queue.pop(0)
        if grid[x][y] == target:
            return steps
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, steps + 1))

    return -1