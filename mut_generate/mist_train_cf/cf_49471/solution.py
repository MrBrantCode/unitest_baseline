"""
QUESTION:
Write a function `shortestPathBinaryMatrix` that takes a binary matrix `grid` of dimensions `n x n` as input and returns the length of the shortest unobstructed path from the top-left cell `(0, 0)` to the bottom-right cell `(n - 1, n - 1)`. If no such path exists, return `-1`. The path should only traverse cells with value `0` and can move in 8 directions (up, down, left, right, and diagonals). The function should run in O(n^2) time complexity and O(n^2) space complexity.
"""

from typing import List
from collections import deque

def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[0][0] or grid[n - 1][n - 1]:
        return -1  # if start or end is blocked
        
    q = deque([(0, 0, 1)])  # queue for BFS, storing (row, col, path length)
        
    # 8 directions to move
    directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

    while q:
        x, y, length = q.popleft()
        if x == y == n - 1:  # If reached end, return path length
            return length
            
        # Explore neighbours
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not grid[nx][ny]:  # If cell is available
                q.append((nx, ny, length + 1))
                grid[nx][ny] = 1  # Mark as visited

    return -1  # If no path found