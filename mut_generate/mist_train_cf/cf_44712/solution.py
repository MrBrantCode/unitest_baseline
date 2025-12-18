"""
QUESTION:
Design a function `minPath(grid, k)` that determines an ordered sequence of the k smallest values route on an NxN grid. The starting point can be any cell, with possible moves to neighboring cells. The function should not exceed the grid boundaries and return an ascending list of k length. The grid is an NxN matrix where each cell holds a unique integer within 1<=N*N.
"""

import heapq

def minPath(grid, k):
    """
    Determine an ordered sequence of the k smallest values route on an NxN grid.

    Args:
    grid (list): An NxN matrix where each cell holds a unique integer within 1<=N*N.
    k (int): The number of smallest values to find.

    Returns:
    list: An ascending list of k length containing the smallest values.
    """
    pq, path, visited = [], [], set()
    n = len(grid)
    heapq.heappush(pq, (grid[0][0], 0, 0))
    while pq:
        val, x, y = heapq.heappop(pq)
        if (x, y) not in visited:
            visited.add((x, y))
            path.append(val)
            if len(path) == k:
                return sorted(path)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < n:
                    heapq.heappush(pq, (grid[new_x][new_y], new_x, new_y))
    return sorted(path)