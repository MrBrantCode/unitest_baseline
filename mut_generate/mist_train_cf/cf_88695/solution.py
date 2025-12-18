"""
QUESTION:
Design a function `navigate_maze(maze: List[List[int]]) -> List[Tuple[int, int]]` that finds the shortest path from the top-left cell (0, 0) to the bottom-right cell (N-1, N-1) in a given N x N maze, where N is a positive integer (1 <= N <= 100). The maze is represented as a 2D grid where each cell can be either 0 (empty) or 1 (blocked). The function should return a list of tuples representing the shortest path from start to end if it exists, otherwise return an empty list. The path should only include adjacent cells that are not blocked, and it should not visit the same cell more than once. The time complexity of the algorithm should be O(N^2) or better.
"""

from typing import List, Tuple

def navigate_maze(maze: List[List[int]]) -> List[Tuple[int, int]]:
    n = len(maze)
    
    # Initialize the visited and distance matrices
    visited = [[False] * n for _ in range(n)]
    distance = [[float('inf')] * n for _ in range(n)]
    previous = [[None] * n for _ in range(n)]
    
    # Define the directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Initialize the queue with the start cell
    queue = [(0, 0)]
    distance[0][0] = 0
    
    # BFS algorithm
    while queue:
        # Remove the first cell from the queue
        cell = queue.pop(0)
        row, col = cell
        
        # Mark the cell as visited
        visited[row][col] = True
        
        # If the cell is the destination cell, stop the algorithm
        if (row, col) == (n-1, n-1):
            break
        
        # Explore the adjacent cells
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            
            # Check if the adjacent cell is valid and not blocked
            if 0 <= new_row < n and 0 <= new_col < n and maze[new_row][new_col] == 0 and not visited[new_row][new_col]:
                # Compute the distance from the start cell to the adjacent cell
                new_distance = distance[row][col] + 1
                
                # Update the distance and add the adjacent cell to the queue
                if new_distance < distance[new_row][new_col]:
                    distance[new_row][new_col] = new_distance
                    previous[new_row][new_col] = (row, col)
                    queue.append((new_row, new_col))
    
    # Reconstruct the path if it exists
    if visited[n-1][n-1]:
        path = [(n-1, n-1)]
        row, col = n-1, n-1
        
        while (row, col) != (0, 0):
            row, col = previous[row][col]
            path.append((row, col))
        
        path.reverse()
        return path
    
    return []