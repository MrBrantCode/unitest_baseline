"""
QUESTION:
Given two integer arrays A and B, write a function `findLength(A, B)` that returns the maximum length of a continuous subarray that appears in both arrays, along with the subarray itself. The function should have a time complexity of O(n^2) or better, where n is the length of the arrays.
"""

def findLength(A, B):
    len_a = len(A)
    len_b = len(B)
    dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    max_length = 0
    subarray = []

    for i in range(len_a - 1, -1, -1):
        for j in range(len_b - 1, -1, -1):
            if A[i] == B[j]:
                dp[i][j] = dp[i+1][j+1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    subarray = A[i:i+max_length]
    return max_length, subarray