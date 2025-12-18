"""
QUESTION:
Write a function called `minimumEffortPath` that takes a 2D list of integers `heights` as input and returns the least amount of exertion needed to traverse from the top-left cell to the bottom-right cell. The exertion of a path is determined by the greatest absolute disparity in altitudes between two successive cells along the path. The function must handle grids with 1 to 100 rows and columns, and each cell's altitude ranges from 1 to 10^6.
"""

import heapq

def minimumEffortPath(heights):
    m, n = len(heights), len(heights[0])
    heap = [(0, 0, 0)]  
    dp = [[float('inf')]*n for _ in range(m)]  
    dp[0][0] = 0
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    
    while heap:
        maxDist, x, y = heapq.heappop(heap)
        if (x, y) == (m-1, n-1):  
            return maxDist
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                cost = max(maxDist, abs(heights[x][y] - heights[nx][ny]))  
                if cost < dp[nx][ny]:  
                    dp[nx][ny] = cost
                    heapq.heappush(heap, (cost, nx, ny))