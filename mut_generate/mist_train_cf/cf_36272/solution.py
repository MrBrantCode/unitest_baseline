"""
QUESTION:
Implement a function `longestCommonSubsequence` that takes two arrays A and B of integers and returns the length of the longest subsequence that appears in both arrays. The function should only consider subsequences that can be derived from the arrays by deleting some or no elements without changing the order of the remaining elements. The arrays A and B may have different lengths.
"""

from typing import List

def longestCommonSubsequence(A: List[int], B: List[int]) -> int:
    n = len(A)
    m = len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]