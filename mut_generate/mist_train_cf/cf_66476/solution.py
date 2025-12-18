"""
QUESTION:
Write a function `MinPath` that takes a 2D grid of integers and an integer `k` as input, and returns a list of `k` integers representing the path with the minimum sum from the bottom-right to the top-left of the grid. The function should use dynamic programming to build a 2D array `dp` where `dp[i, j]` represents the minimum sum from the top-left to the cell at `(i, j)`. The function should then use `dp` to construct the path by starting at the bottom-right and moving up or left at each step, and return the path in ascending order. If `k` is greater than the total number of cells in the grid, return an empty list. The function should handle the case where the input grid is null or empty.
"""

def minPath(grid, k):
    if not grid or not grid[0]:
        return []

    n = len(grid)
    if k > n * n:
        return []

    dp = [[0] * n for _ in range(n)]
    dp[0][0] = grid[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
        dp[0][i] = dp[0][i - 1] + grid[0][i]

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    path = []
    i, j = n - 1, n - 1
    while len(path) < k:
        path.append(grid[i][j])
        if i > 0 and j > 0:
            if dp[i - 1][j] < dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        elif i > 0:
            i -= 1
        elif j > 0:
            j -= 1
        else:
            break

    path.sort()
    return path