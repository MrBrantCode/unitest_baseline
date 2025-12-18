"""
QUESTION:
Write a function `longestCommonSubsequence(s, t)` that takes two strings `s` and `t` as input and returns the length of the longest common subsequence between them. The function should not use any built-in functions for finding longest common subsequences. The function should work in O(m*n) time complexity where m and n are the lengths of strings s and t respectively.
"""

def longestCommonSubsequence(s, t):
    m, n = len(s), len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]