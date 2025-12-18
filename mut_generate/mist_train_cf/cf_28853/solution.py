"""
QUESTION:
Complete the `day13` function to find the shortest path from a starting point to an exit in a given maze. The function should take a 2D list `maze`, a starting point `start` as a tuple `(x, y)`, and an exit point `exit` as a tuple `(x, y)` as input. The maze is represented as a grid, where 0 represents an empty cell and 1 represents a wall. The function should return the number of steps taken to reach the exit if a path exists, and -1 otherwise. The `check_wall` function is not required for this task.
"""

from collections import deque

def day13(maze, start, exit):
    queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == exit:
            return steps  # Return the number of steps taken to reach the exit

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                queue.append((new_x, new_y, steps + 1))

    return -1  # If no path to the exit is found