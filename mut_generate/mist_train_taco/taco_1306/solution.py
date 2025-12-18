"""
QUESTION:
Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is not equal to another (not rotated or reflected).
Example 1:
Input:
grid[][] = {{1, 1, 0, 0, 0},
            {1, 1, 0, 0, 0},
            {0, 0, 0, 1, 1},
            {0, 0, 0, 1, 1}}
Output:
1
Explanation:
grid[][] = {{1, 1, 0, 0, 0}, 
            {1, 1, 0, 0, 0}, 
            {0, 0, 0, 1, 1}, 
            {0, 0, 0, 1, 1}}
Same colored islands are equal.
We have 2 equal islands, so we 
have only 1 distinct island.
Example 2:
Input:
grid[][] = {{1, 1, 0, 1, 1},
            {1, 0, 0, 0, 0},
            {0, 0, 0, 0, 1},
            {1, 1, 0, 1, 1}}
Output:
3
Explanation:
grid[][] = {{1, 1, 0, 1, 1}, 
            {1, 0, 0, 0, 0}, 
            {0, 0, 0, 0, 1}, 
            {1, 1, 0, 1, 1}}
Same colored islands are equal.
We have 4 islands, but 2 of them
are equal, So we have 3 distinct islands.
Your Task:
You don't need to read or print anything. Your task is to complete the function countDistinctIslands() which takes the grid as an input parameter and returns the total number of distinct islands.
Expected Time Complexity: O(n * m)
Expected Space Complexity: O(n * m)
Constraints:
1 ≤ n, m ≤ 500
grid[i][j] == 0 or grid[i][j] == 1
"""

import sys
from typing import List

sys.setrecursionlimit(10 ** 8)

def count_distinct_islands(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    vis = [[False] * n for _ in range(m)]
    res = set()
    
    def dfs(i, j, l, row0, col0):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or vis[i][j]:
            return
        vis[i][j] = True
        l.append((i - row0, j - col0))
        dfs(i - 1, j, l, row0, col0)
        dfs(i, j - 1, l, row0, col0)
        dfs(i + 1, j, l, row0, col0)
        dfs(i, j + 1, l, row0, col0)
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not vis[i][j]:
                l = []
                dfs(i, j, l, i, j)
                res.add(tuple(l))
    
    return len(res)