"""
QUESTION:
You are given an n x m binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
Find the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
Example 1:
Input:
grid[][] = {{0, 0, 0, 0},
            {1, 0, 1, 0},
            {0, 1, 1, 0},
            {0, 0, 0, 0}}
Output:
3
Explanation:
0 0 0 0
1 0 1 0
0 1 1 0
0 0 0 0
The highlighted cells represents the land cells.
Example 2:
Input:
grid[][] = {{0, 0, 0, 1},
            {0, 1, 1, 0},
            {0, 1, 1, 0},
            {0, 0, 0, 1},
            {0, 1, 1, 0}}
Output:
4
Explanation:
0 0 0 1
0 1 1 0
0 1 1 0
0 0 0 1
0 1 1 0
The highlighted cells represents the land cells.
Your Task:
You don't need to print or input anything. Complete the function numberOfEnclaves() which takes a 2D integer matrix grid as the input parameter and returns an integer, denoting the number of land cells.
Expected Time Complexity: O(n * m)
Expected Space Complexity: O(n * m)
Constraints:
	1 <= n, m <= 500
	grid[i][j] == 0 or 1
"""

from typing import List

def count_enclosed_land_cells(grid: List[List[int]]) -> int:
    num_ones = 0
    ones = []
    visited = set()
    n = len(grid)
    m = len(grid[0])
    
    # Count all land cells and mark boundary land cells
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                num_ones += 1
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    ones.append((i, j))
                    visited.add((i, j))
    
    # Traverse from boundary land cells and mark reachable land cells
    while ones:
        x = ones.pop(0)
        num_ones -= 1
        a1, a2 = x
        
        # Check adjacent cells
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = a1 + dx, a2 + dy
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1 and (ni, nj) not in visited:
                ones.append((ni, nj))
                visited.add((ni, nj))
    
    return num_ones