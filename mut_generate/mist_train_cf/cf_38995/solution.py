"""
QUESTION:
Implement a method `minPathSum(self, grid: List[List[int]]) -> int` to calculate the minimum path sum from the top-left cell to the bottom-right cell in a grid. The grid is a 2D list of integers, where each element represents the cost to traverse that cell. Movement is restricted to only right or down. Return the minimum path sum as an integer.
"""

from typing import List
import heapq

def minPathSum(grid: List[List[int]]) -> int:
    """
    Calculate the minimum path sum from the top-left cell to the bottom-right cell in a grid.
    
    Args:
    grid (List[List[int]]): A 2D list of integers representing the cost to traverse each cell.
    
    Returns:
    int: The minimum path sum as an integer.
    """
    
    m, n = len(grid), len(grid[0])
    distance = [[float('inf')] * n for _ in range(m)]
    distance[0][0] = grid[0][0]  # Initialize the top-left cell
    
    directions = [(1, 0), (0, 1)]  # Down and right movements
    
    for i in range(m):
        for j in range(n):
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < m and 0 <= nc < n:
                    distance[nr][nc] = min(distance[nr][nc], distance[i][j] + grid[nr][nc])
    
    return distance[m - 1][n - 1]  # Return the minimum path sum