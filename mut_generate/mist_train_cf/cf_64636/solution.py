"""
QUESTION:
Implement a function named `minPath` that takes a 2D grid and an integer `k` as input, and returns the minimum path of length `k` in the grid. The function should use a priority queue to traverse the grid and return the path with the smallest values. The grid is a square of size `n x n`, where `n` is the number of rows (or columns) in the grid. The function should return the path of length `k` with the smallest values. If the entire grid is traversed and `k` cells have not been visited, return the path so far.
"""

import heapq

def minPath(grid, k):
    pq, path, visited = [], [], set()
    n = len(grid)
    pq.append((grid[0][0], 0, 0))
    while pq:
        val, x, y = heapq.heappop(pq)
        if (x, y) not in visited:
            visited.add((x, y))
            path.append(val)
            if len(path) == k:
                return path
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < n:
                    heapq.heappush(pq, (grid[new_x][new_y], new_x, new_y))
    return path