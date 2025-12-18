"""
QUESTION:
Implement the function `minFallingPath(matrix)` that takes an `n x n` array of integers as input. The function should return the minimum sum of any falling path through the matrix, considering that a falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right, and that some elements in the matrix are marked as obstacles (represented by -1). If an obstacle is encountered, a different path must be chosen, and if no path is available, return -1. The constraints are `n == matrix.length`, `n == matrix[i].length`, `1 <= n <= 100`, and `-100 <= matrix[i][j] <= 100` or `matrix[i][j] == -1`.
"""

def minFallingPath(matrix):
    n = len(matrix)
    dp = [[float('inf')]*n for _ in range(n)]
    dp[0] = matrix[0]
    
    for i in range(1, n):
        for j in range(n):
            if matrix[i][j] != -1:
                if j > 0 and dp[i-1][j-1] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + matrix[i][j])
                if dp[i-1][j] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + matrix[i][j])
                if j < n-1 and dp[i-1][j+1] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1] + matrix[i][j])
        
        if all(val == float('inf') for val in dp[i]):
            return -1
    
    return min(dp[-1])