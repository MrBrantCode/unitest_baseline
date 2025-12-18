"""
QUESTION:
Write a function `orangesRotting` that takes a 2D grid where 0 represents an empty cell, 1 represents a fresh orange, and 2 represents a rotten orange. The function should return the minimum number of minutes until no fresh oranges are left, or -1 if it's impossible for all oranges to rot. 

The grid is guaranteed to be non-empty and all cells are initially either 0, 1, or 2.
"""

from collections import deque

def orangesRotting(grid):
    # Initialize variables
    fresh = 0
    minutes = -1
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    queue = deque()

    # Process initial grid and setup the decayed queue along with the fresh count
    for i in range(len(grid)):
       for j in range(len(grid[0])):
           if grid[i][j] == 2:
               queue.append((i, j))
           elif grid[i][j] == 1:
               fresh += 1

    # BFS through the grid
    while queue and fresh:
       minutes += 1
       for _ in range(len(queue)):
           x, y = queue.popleft()

           for dx, dy in directions:
               nx, ny = x + dx, y + dy

               if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != 1:
                   continue

               fresh -= 1
               grid[nx][ny] = 2
               queue.append((nx, ny))

    return minutes if fresh == 0 else -1