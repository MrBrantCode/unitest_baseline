"""
QUESTION:
Write a function `largest_square_submatrix(matrix)` that takes as input an n x n matrix where each element is 0 or 1, and returns the area of the largest square sub-matrix composed of only '1s'. The function should have a time complexity of O(n^2) and a space complexity of O(n).
"""

def largest_square_submatrix(matrix):
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]
    
    # Copy first row and first column
    for i in range(n):
        dp[i][0] = matrix[i][0]
        dp[0][i] = matrix[0][i]
    
    max_size = 0
    for i in range(1, n):
        for j in range(1, n):
            if matrix[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                max_size = max(max_size, dp[i][j])
    
    return max_size * max_size