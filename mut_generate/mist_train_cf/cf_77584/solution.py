"""
QUESTION:
Given an integer matrix `isWater` of dimensions `m x n` where `0` represents land cells and `1` represents water cells, write a function `highestPeak` that assigns a non-negative height to each cell such that the absolute difference in height between any two adjacent cells does not exceed 1 and water cells have a height of 0. The function should return an integer matrix `height` of dimensions `m x n` representing the assigned heights. The constraints are:

- `m == isWater.length`
- `n == isWater[i].length`
- `1 <= m, n <= 1000`
- `isWater[i][j]` is either `0` or `1`
- At least one water cell exists
"""

from collections import deque

def highestPeak(isWater):
    m = len(isWater)
    n = len(isWater[0])

    height = [[float('inf')]*n for _ in range(m)]
    Q = deque([])

    # Add all water cells to the queue and set their heights to 0
    for i in range(m):
        for j in range(n):
            if isWater[i][j] == 1:
                height[i][j] = 0
                Q.append((i, j))
                
    # List all the four possible directions a cell can have
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while Q:
        a, b = Q.popleft()
        for d in directions:
            c = a + d[0]
            d = b + d[1]
          
            if 0<=c<m and 0<=d<n and height[a][b] + 1 < height[c][d]:
                height[c][d] = height[a][b] + 1
                Q.append((c, d))

    return height