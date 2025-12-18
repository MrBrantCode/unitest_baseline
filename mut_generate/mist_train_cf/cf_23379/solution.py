"""
QUESTION:
Create a function `find_shortest_path` that takes a 2D list `maze` as input where 0 represents an open space and 1 represents a wall. The function should return the length of the shortest path from the top-left corner to the bottom-right corner, or infinity if there is no path. The path can only be constructed from open spaces (0) and can move in four directions (up, down, left, right).
"""

from collections import deque

def find_shortest_path(maze):
    """
    This function finds the length of the shortest path from the top-left corner 
    to the bottom-right corner in a given 2D maze. The maze is represented as a 
    2D list where 0 represents an open space and 1 represents a wall. The path 
    can only be constructed from open spaces and can move in four directions 
    (up, down, left, right).

    Args:
        maze (list): A 2D list representing the maze.

    Returns:
        int: The length of the shortest path. If there is no path, returns infinity.
    """
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set((0, 0))
    queue = deque([(0, 0, 1)])

    while queue:
        x, y, length = queue.popleft()
        
        # Reached the end
        if x == rows - 1 and y == cols - 1:
            return length

        # Add neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows) and (0 <= ny < cols) and maze[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny, length + 1))
                visited.add((nx, ny))

    return float('inf')