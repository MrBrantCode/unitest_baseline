"""
QUESTION:
Determine the maximum sum that can be acquired by traversing exactly k cells of a square grid of dimension N x N, where the grid distance between two cells follows the Chess King's movements. The grid is filled with unique integers between 1 and N*N, inclusive, and starting and ending points can be any arbitrary cells. Implement a function maxSumPathChess(grid, k) that returns the maximum sum.

Restrictions: 
- Grid is a 2D list of unique integers.
- k is an integer representing the number of cells to traverse.
- Function should return the maximum sum that can be acquired by traversing k cells.
"""

def maxSumPathChess(grid, k):
    n = len(grid)
    dp = [[[-1 for _ in range(n*n)] for _ in range(n)] for _ in range(n)]
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, -1, 1, -1, 1]

    def maxSum(x, y, steps):
        if steps == k:
            return grid[x][y]

        if dp[x][y][steps] != -1:
            return dp[x][y][steps]

        max_path = 0
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                max_path = max(max_path, maxSum(nx, ny, steps+1))

        dp[x][y][steps] = max_path + grid[x][y]
        return dp[x][y][steps]

    result = 0
    for i in range(n):
        for j in range(n):
            result = max(result, maxSum(i, j, 0))

    return result