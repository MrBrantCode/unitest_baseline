"""
QUESTION:
Write a function `trapRainWater` that takes a 2D elevation map `heightMap` of size `m x n` as input and returns the volume of water it can trap after raining. The elevation map contains positive integers representing the height of each unit cell, and some cells may have obstacles represented by a negative integer. The function should handle obstacles while calculating the total volume of trapped water. The elevation map constraints are `1 <= m, n <= 110` and `-1 <= heightMap[i][j] <= 20000`.
"""

from heapq import heappush, heappop
def trapRainWater(heightMap):
    if not heightMap or not heightMap[0]:
        return 0
    
    m, n = len(heightMap), len(heightMap[0])
    heap = []
    visited = [[0]*n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0 or i == m-1 or j == n-1 or heightMap[i][j] == -1:
                heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = 1
                
    trapped = 0
    while heap:
        height, i, j = heappop(heap)
        for x, y in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
            if 0 <= x < m and 0 <= y < n and not visited[x][y] and heightMap[x][y] != -1:
                trapped += max(0, height-heightMap[x][y])
                heappush(heap, (max(heightMap[x][y],height), x, y))
                visited[x][y] = 1
                
    return trapped