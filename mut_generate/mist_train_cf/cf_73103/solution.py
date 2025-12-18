"""
QUESTION:
Write a function `minPathSumSequence(grid, k)` that takes a 2D N x N matrix `grid` and an integer `k` as input. The function should return the sequence of `k` steps with the minimum sum in the matrix. Movement is only allowed to cells that are either horizontally or vertically adjacent, and each cell has a unique integer between 1 and N^2.
"""

import heapq

def minPathSumSequence(grid, k):
    N = len(grid)
    minheap = [(grid[0][0], 0, 0)]
    dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]

    def valid(x, y):
        return 0 <= x < N and 0 <= y < N
    
    visited = [[0]*N for _ in range(N)]
    sequence = [grid[0][0]]
    
    while minheap and len(sequence) < k:
        min_dist, x, y = heapq.heappop(minheap)
        if visited[x][y] == 1:
            continue
        visited[x][y] = 1
        for dx, dy in dirs:
            newX, newY = x + dx, y + dy
            if valid(newX, newY) and visited[newX][newY] == 0:
                heapq.heappush(minheap, (grid[newX][newY], newX, newY))
        if len(minheap) > 0:
            sequence.append(minheap[0][0])
    return sequence