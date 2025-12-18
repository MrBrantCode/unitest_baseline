"""
QUESTION:
Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands.
Note: An island is either surrounded by water or boundary of grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.
Example 1:
Input:
grid = {{0,1},{1,0},{1,1},{1,0}}
Output:
1
Explanation:
The grid is-
0 1
1 0
1 1
1 0
All lands are connected.
Example 2:
Input:
grid = {{0,1,1,1,0,0,0},{0,0,1,1,0,1,0}}
Output:
2
Expanation:
The grid is-
0 1 1 1 0 0 0
0 0 1 1 0 1 0 
There are two islands :- one is colored in blue 
and other in orange.
Your Task:
You don't need to read or print anything. Your task is to complete the function numIslands() which takes the grid as an input parameter and returns the total number of islands.
Expected Time Complexity: O(n*m)
Expected Space Complexity: O(n*m)
Constraints:
1 ≤ n, m ≤ 500
"""

def count_islands(grid):
    if not grid or not grid[0]:
        return 0

    (m, n) = (len(grid), len(grid[0]))

    def dfs(row, col):
        if row < 0 or row >= m or col < 0 or col >= n:
            return
        if grid[row][col] == 1:
            grid[row][col] = 0
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)
            dfs(row + 1, col + 1)
            dfs(row - 1, col - 1)
            dfs(row - 1, col + 1)
            dfs(row + 1, col - 1)

    island_count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                island_count += 1
                dfs(i, j)

    return island_count