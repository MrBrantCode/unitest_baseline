"""
QUESTION:
Given two integer arrays A and B, find the maximum length of a continuous subarray that appears in both arrays without containing any repeating elements, and return the subarray itself. Implement the function findLength(A, B) with a time complexity of O(n^2) or better and a space complexity of O(n) or better.
"""

def findLength(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len, max_end = 0, 0
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if A[i] == B[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    max_end = i
    return A[max_end:max_end + max_len]