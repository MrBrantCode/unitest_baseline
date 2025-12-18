"""
QUESTION:
Given a 2D array of size N x N where each cell contains a distinct integer from 1 to N^2, and a positive integer k, write a function `minPathSumSequence(grid, k)` to find the sequence of numbers that sums up to the minimum possible sum with a path of k steps, where each step can move horizontally or vertically to an adjacent cell. The function should return an empty list if no such path exists.
"""

import heapq

def minPathSumSequence(grid, k):
    N = len(grid)
    if k < N * N:
        dp = [[[float('inf')] * k for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                dp[i][j][0] = grid[i][j]

        pq = [(grid[0][0], 0, 0, 0)]

        while pq:
            curr_sum, x, y, steps = heapq.heappop(pq)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if steps + 1 < k and curr_sum + grid[nx][ny] < dp[nx][ny][steps + 1]:
                        dp[nx][ny][steps + 1] = curr_sum + grid[nx][ny]
                        heapq.heappush(pq, (dp[nx][ny][steps + 1], nx, ny, steps + 1))

        min_sum = min(dp[i][j][k - 1] for i in range(N) for j in range(N))
        if min_sum == float('inf'):
            return []
        
        # backtrack and construct the path
        path = []
        for step in range(k - 1, -1, -1):
            for i in range(N):
                for j in range(N):
                    if dp[i][j][step] == min_sum:
                        path.append(grid[i][j])
                        min_sum -= grid[i][j]
                        break
                else:
                    continue
                break
        return list(reversed(path))

    else:
        return "The number of steps is larger than the number of cells in the grid."