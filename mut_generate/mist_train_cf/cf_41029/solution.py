"""
QUESTION:
Write a function `countDistinctIslands` that takes a 2D binary matrix of size N x N as input, where 1 represents land and 0 represents water, and returns the number of distinct islands present in the map, where two lands are considered connected if they are adjacent horizontally or vertically. The function should consider the shape of the islands, not their positions in the map.
"""

from typing import List

def countDistinctIslands(grid: List[List[int]]) -> int:
    def dfs(i, j, path, direction):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return '0'
        grid[i][j] = 0
        path += direction
        path = dfs(i+1, j, path, 'D')
        path = dfs(i-1, j, path, 'U')
        path = dfs(i, j+1, path, 'R')
        path = dfs(i, j-1, path, 'L')
        return path + '0'

    distinct_islands = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                island_shape = dfs(i, j, '', 'X')
                distinct_islands.add(island_shape)
    return len(distinct_islands)