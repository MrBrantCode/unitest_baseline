"""
QUESTION:
Write a function `longest_common_substring(A, B)` that takes two strings `A` and `B` as input and returns the length of their longest common substring. The function should have a time complexity of O(n^2), where n is the length of the longer string.
"""

def longest_common_substring(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n+1) for _ in range(m+1)]
    max_length = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_length = max(max_length, dp[i][j])

    return max_length