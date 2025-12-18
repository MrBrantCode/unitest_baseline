"""
QUESTION:
Write a function `uncrossed_lines(A, B)` that takes two lists of integers `A` and `B` as input, where `1 <= len(A) <= 500`, `1 <= len(B) <= 500`, and `1 <= A[i], B[i] <= 2000`. The function should return the maximum number of uncrossed lines that can be drawn between the elements of `A` and `B` without any intersections, where a line can be drawn between two elements if they are equal and do not intersect with any other line.
"""

def maxUncrossedLines(A, B):
    m, n = len(A), len(B)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] = max(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1] + (A[i] == B[j]))
    return dp[0][0]