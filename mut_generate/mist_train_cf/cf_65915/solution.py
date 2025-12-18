"""
QUESTION:
Design a function `minSumPath(grid, k)` to find the k smallest sums of weights for all possible paths from any starting point to any other point on an NxN grid, with constraints that movements can only be horizontal or vertical and must not exceed the grid boundaries. The function should return an ascending list of k length, where each number in the list represents the sum of weights of a chosen path. The grid is represented as a 2D list where each cell holds a unique integer between 1 and N*N.
"""

import heapq

def minSumPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = grid[0][0]
    queue = [(grid[0][0], 0, 0)]
    result = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    while queue and len(result) < k:
        cur_sum, i, j = heapq.heappop(queue)
        result.append(cur_sum)

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                new_sum = cur_sum + grid[ni][nj]
                if new_sum < dp[ni][nj]:
                    dp[ni][nj] = new_sum
                    heapq.heappush(queue, (new_sum, ni, nj))

    return result