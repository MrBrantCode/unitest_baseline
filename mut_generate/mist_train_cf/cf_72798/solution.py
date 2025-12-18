"""
QUESTION:
Write a function `pathFinder(grid, k)` that takes a 2D grid of unique positive integers and an integer `k` as input, and returns a list of the minimum cumulative value of exactly `k` cells in ascending order. The function should explore the grid by moving to any neighboring cells, including diagonals. The grid is a square of size `N x N` where `N` is not less than 3.
"""

import heapq

def pathFinder(grid, k):
    n = len(grid)
    directions = [(0,1), (0,-1), (1,0), (-1,0), (-1,-1), (-1,1), (1,-1), (1,1)]
    heap = [(grid[0][0], 0, 0)]
    visit = [[0 for _ in range(n)] for _ in range(n)]
    visit[0][0] = 1
    cell_values = []

    while heap:
        value, x, y = heapq.heappop(heap)
        cell_values.append(value)
        if len(cell_values) == k:
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                visit[nx][ny] = 1
                heapq.heappush(heap, (grid[nx][ny], nx, ny))

    return sorted(cell_values[:k])