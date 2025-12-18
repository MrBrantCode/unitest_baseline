"""
QUESTION:
Implement a function `find_shortest_path` that finds the shortest path from a starting position to a goal position in a grid-based environment. The function takes a 2D grid, the starting position, and the goal position as input. The grid is represented as a 2D list where 0 represents an empty cell and 1 represents an obstacle. The starting and goal positions are tuples representing the row and column of the grid cell. The function returns a list of tuples representing the shortest path from the starting position to the goal position. If no path exists, the function returns an empty list. The vehicle can move in four directions: up, down, left, and right.
"""

from typing import List, Tuple
from collections import deque

def find_shortest_path(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                queue.append(((new_x, new_y), path + [(new_x, new_y)]))
                visited.add((new_x, new_y))

    return []