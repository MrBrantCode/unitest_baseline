"""
QUESTION:
Write a function `find_max_path_sum` that takes a 2D array of positive integers as input and returns the maximum sum of a path from the top left cell to the bottom right cell. The path can only move downwards or rightwards, and each cell can only be visited once. The path must include at least one cell with an odd number and one cell with an even number, and it must avoid any prime numbers.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_max_path_sum(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    dp = [[0 for _ in range(n)] for _ in range(m)]
    
    dp[0][0] = matrix[0][0]
    
    for i in range(1, m):
        if is_prime(matrix[i][0]):
            dp[i][0] = -1
        else:
            dp[i][0] = dp[i-1][0] + matrix[i][0]
    
    for j in range(1, n):
        if is_prime(matrix[0][j]):
            dp[0][j] = -1
        else:
            dp[0][j] = dp[0][j-1] + matrix[0][j]
    
    for i in range(1, m):
        for j in range(1, n):
            if is_prime(matrix[i][j]):
                dp[i][j] = -1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    
    return dp[m-1][n-1]