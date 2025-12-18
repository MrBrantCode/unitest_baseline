"""
QUESTION:
Given two strings `text1` and `text2` consisting of lowercase English characters, write a function `longestCommonSubsequence` that returns the length of the longest common subsequence shared by `text1` and `text2`. The function should take two parameters: `text1` and `text2`, and return an integer value. The length of `text1` and `text2` is between 1 and 1000, inclusive.
"""

def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)  
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]: 
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]