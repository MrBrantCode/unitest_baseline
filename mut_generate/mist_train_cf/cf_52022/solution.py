"""
QUESTION:
Write a function `maximalSquare(matrix)` that takes a 2D grid of binary strings as input and returns the area of the largest square containing only '1's. The grid is `m x n` in size, where `m` and `n` are between 0 and 200 (inclusive). Each cell in the grid contains either '0' or '1'.
"""

def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if len(matrix) == 0:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    max_side = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if matrix[i-1][j-1] == "1":
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    return max_side * max_side