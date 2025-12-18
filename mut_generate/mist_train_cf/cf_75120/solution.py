"""
QUESTION:
Given two sets of integers `A` and `B`, find the maximum number of non-intersecting lines that can be drawn between the numbers in `A` and `B` where the lines are only allowed to connect equal numbers and do not intersect with each other.

Write a function `maxUncrossedLines(A, B)` that takes two lists of integers `A` and `B` as input and returns the maximum number of non-intersecting lines.

Constraints:
- 1 ≤ len(A) ≤ 500
- 1 ≤ len(B) ≤ 500
- 1 ≤ A[i], B[i] ≤ 2000
"""

def maxUncrossedLines(A, B):
    N, M = len(A), len(B)
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            if A[i] == B[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[-1][-1]