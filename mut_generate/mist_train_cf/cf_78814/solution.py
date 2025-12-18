"""
QUESTION:
Design a function named minPath that finds the shortest sequence of k elements within an NxN grid, where N is 2 or greater. The grid contains distinct integers from 1 to N^2, and each element in the sequence must be a neighboring element in the grid (horizontally or vertically adjacent). The function should return the shortest sequence of k elements.
"""

import heapq

def minPath(grid, k):
    # size of the grid
    N = len(grid)
    # Priority Queue
    minheap = [(grid[0][0], 0, 0, [grid[0][0]])]
    visited = set([(0, 0)])

    # iterating over all the elements in Priority Queue
    while minheap:
        cost, i, j, path = heapq.heappop(minheap)
        # checking if the path size is k
        if len(path) == k:
            return path[:k]
        # checking all the neighbors of the current node
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < N and 0 <= y < N and (x, y) not in visited:
                visited.add((x, y))
                new_cost = cost + grid[x][y]
                new_path = path + [grid[x][y]]
                heapq.heappush(minheap, (new_cost, x, y, new_path))