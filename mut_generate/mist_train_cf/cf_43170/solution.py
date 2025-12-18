"""
QUESTION:
You are given a 2D grid representing a maze with start 'S', end 'E', open passages ' ', and walls '#'. Implement a function `shortestPath` that returns the length of the shortest path from 'S' to 'E' by moving vertically or horizontally through open passages. If no path exists, return -1. The maze is surrounded by walls and 'S' and 'E' are guaranteed to be open passages.
"""

from typing import List
from collections import deque

def shortestPath(maze: List[List[str]]) -> int:
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    start_row, start_col = 0, 0
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start_row, start_col = i, j
                break

    queue = deque([(start_row, start_col, 0)])
    visited = set((start_row, start_col))

    while queue:
        row, col, distance = queue.popleft()

        if maze[row][col] == 'E':
            return distance

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] != '#':
                if (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, distance + 1))
                new_row, new_col = new_row + dr, new_col + dc

    return -1