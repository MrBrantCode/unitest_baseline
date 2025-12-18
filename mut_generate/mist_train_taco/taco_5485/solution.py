"""
QUESTION:
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.
The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
If no land or water exists in the grid, return -1.
 
Example 1:

Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:

Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.

 
Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1
"""

from collections import deque
from typing import List

def max_distance_to_land(grid: List[List[int]]) -> int:
    queue = deque()
    n = len(grid)
    
    # Initialize the queue with all land cells
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                queue.append((i, j, 0))  # (i, j) is the position, 0 is the initial distance
    
    # If there is no land or no water, return -1
    if len(queue) == 0 or len(queue) == n * n:
        return -1
    
    dist = {}
    
    # Perform BFS
    while queue:
        (i, j, d) = queue.popleft()
        
        if (i, j) not in dist:
            dist[(i, j)] = d
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in dist:
                    queue.append((ni, nj, d + 1))
    
    # Find the maximum distance
    max_dist = max(dist.values(), default=-1)
    return max_dist