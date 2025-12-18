"""
QUESTION:
Implement a function `solve` that takes a 2D grid representing a maze as input. Each cell in the grid can be 'S' (starting point), 'E' (ending point), '.' (open path), or '#' (wall). The function should return the length of the shortest path from 'S' to 'E' using a breadth-first search algorithm. If no path exists, return -1.
"""

from collections import deque

def solve(grid):
    """
    This function takes a 2D grid representing a maze as input and returns the length of the shortest path from 'S' to 'E' using a breadth-first search algorithm. If no path exists, it returns -1.

    Args:
        grid (list): A 2D list representing the maze. Each cell can be 'S' (starting point), 'E' (ending point), '.' (open path), or '#' (wall).

    Returns:
        int: The length of the shortest path from 'S' to 'E' if a path exists, -1 otherwise.
    """
    queue = deque()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                queue.append((i, j, 0))  # (x, y, distance)
                break

    while queue:
        x, y, distance = queue.popleft()

        if grid[x][y] == 'E':
            return distance

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] != '#' and grid[new_x][new_y] != 'v':
                queue.append((new_x, new_y, distance + 1))
                grid[new_x][new_y] = 'v'

    return -1