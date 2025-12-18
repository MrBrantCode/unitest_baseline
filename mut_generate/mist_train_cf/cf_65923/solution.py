"""
QUESTION:
Assign a non-negative height to each cell in the integer matrix `isWater` of size `m x n`, where `0` represents land and `1` represents water. Water cells must have a height of `0`, and the absolute difference in height between adjacent cells should not exceed `1`. Return an integer matrix `height` of size `m x n` where `height[i][j]` represents the height of cell `(i, j)` such that the highest point in the matrix is maximized. 

Constraints: 
- `m == isWater.length`
- `n == isWater[i].length`
- `1 <= m, n <= 1000`
- `isWater[i][j]` is `0` or `1`
- At least one water cell is guaranteed to be present.
"""

from collections import deque

def highestPeak(isWater):
    m, n = len(isWater), len(isWater[0])
    dirn = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Initialize the queue and height matrix
    q = deque()
    height = [[float('inf')] * n for _ in range(m)]
    
    # Add all water cells to queue and set their height to 0
    for i in range(m):
        for j in range(n):
            if isWater[i][j] == 1:
                q.append((i, j, 0))
                height[i][j] = 0
    
    # Perform BFS
    while q:
        x, y, h = q.popleft()
        for dx, dy in dirn:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < m and ny >= 0 and ny < n and height[nx][ny] > h + 1:
                height[nx][ny] = h + 1
                q.append((nx, ny, h + 1))
    
    return height