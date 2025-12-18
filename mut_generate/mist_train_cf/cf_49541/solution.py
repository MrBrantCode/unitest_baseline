"""
QUESTION:
Write a function `count_unique_paths` that calculates the number of unique paths from a given start point (px, py) to a goal point (gx, gy) in an NxM grid. The function should take as input a 2D grid (or its dimensions N and M), start point (px, py), and goal point (gx, gy). You can move in one of four directions: up, down, left, or right, and you cannot revisit a cell once you have moved away from it. Assume that the start and goal points are valid and reachable, and that grid indices start from 1.
"""

def count_unique_paths(N, M, start, goal):
    """
    Calculate the number of unique paths from a given start point to a goal point in an NxM grid.

    Args:
        N (int): The number of rows in the grid.
        M (int): The number of columns in the grid.
        start (tuple): The start point (px, py).
        goal (tuple): The goal point (gx, gy).

    Returns:
        int: The number of unique paths from start to goal.
    """
    visited = [[False for _ in range(M+1)] for _ in range(N+1)]

    def dfs(px, py):
        # Check if start is out of the grid or visited
        if px < 1 or px > N or py < 1 or py > M or visited[px][py]:
            return 0

        # Check if start is the goal
        if (px, py) == goal:
            return 1

        # Set start as visited
        visited[px][py] = True

        paths = (
            dfs(px-1, py) +
            dfs(px+1, py) +
            dfs(px, py-1) +
            dfs(px, py+1)
        )

        # Mark this cell as not visited for other recursive calls
        visited[px][py] = False

        return paths

    return dfs(*start)