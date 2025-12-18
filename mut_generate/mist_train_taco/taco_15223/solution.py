"""
QUESTION:
Given a grid of dimension nxm containing 0s and 1s. Find the unit area of the largest region of 1s.
Region of 1's is a group of 1's connected 8-directionally (horizontally, vertically, diagonally).
 
Example 1:
Input: grid = {{1,1,1,0},{0,0,1,0},{0,0,0,1}}
Output: 5
Explanation: The grid is-
1 1 1 0
0 0 1 0
0 0 0 1
The largest region of 1's is colored
in orange.
Example 2:
Input: grid = {{0,1}}
Output: 1
Explanation: The grid is-
0 1
The largest region of 1's is colored in 
orange.
Your Task:
You don't need to read or print anyhting. Your task is to complete the function findMaxArea() which takes grid as input parameter and returns the area of the largest region of 1's.
Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)
 
Constraints:
1 ≤ n, m ≤ 500
"""

def find_max_area(grid):
    def dfs(x, y):
        moves = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 1), (-1, 1), (1, 0), (1, 1)]
        stack = [(x, y)]
        count = 0
        while stack:
            cx, cy = stack.pop()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            count += 1
            for dx, dy in moves:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
                    stack.append((nx, ny))
        return count

    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]
    max_area = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                region_area = dfs(i, j)
                if region_area > max_area:
                    max_area = region_area

    return max_area