"""
QUESTION:
Write a function `max_sum_path` that takes a 2D matrix of positive integers as input. The function should find a path from the top-left corner to the bottom-right corner that maximizes the sum of numbers. The path can only move right, down, or diagonally right-down. Each step in the path must be to a position that is either a prime number or a multiple of 3, and no position can be visited twice. The function should return the maximum sum of such a path.
"""

def max_sum_path(matrix):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    n = len(matrix)
    m = len(matrix[0])

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = matrix[0][0]

    for j in range(1, m):
        if is_prime(matrix[0][j]) or matrix[0][j] % 3 == 0:
            dp[0][j] = dp[0][j-1] + matrix[0][j]

    for i in range(1, n):
        if is_prime(matrix[i][0]) or matrix[i][0] % 3 == 0:
            dp[i][0] = dp[i-1][0] + matrix[i][0]

    for i in range(1, n):
        for j in range(1, m):
            if is_prime(matrix[i][j]) or matrix[i][j] % 3 == 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + matrix[i][j]

    return max(dp[n-1])