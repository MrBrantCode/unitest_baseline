"""
QUESTION:
Write a function `minOperations(A, B)` that takes two strings A and B consisting of lowercase English letters and returns the minimum number of operations (insertion, deletion, or substitution of a single character) required to make the two strings equal.
"""

def minOperations(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = i + j
            elif A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]