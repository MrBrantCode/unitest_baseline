"""
QUESTION:
You are given three strings `text1`, `text2`, and `text3`, each consisting of lowercase English alphabets. Write a function `longestCommonSubsequence(text1, text2, text3)` to find the length of the longest common subsequence among these strings. The function should return `0` if no common subsequence exists. The constraints are `1 <= text1.length, text2.length, text3.length <= 1000`.
"""

def longestCommonSubsequence(text1, text2, text3):
    n1, n2, n3 = len(text1), len(text2), len(text3)
    dp = [[[0 for _ in range(n3+1)] for _ in range(n2+1)] for _ in range(n1+1)]

    for i in range(n1-1, -1, -1):
        for j in range(n2-1, -1, -1):
            for k in range(n3-1, -1, -1):
                if text1[i] == text2[j] == text3[k]:
                    dp[i][j][k] = dp[i+1][j+1][k+1] + 1
                else:
                    dp[i][j][k] = max(dp[i+1][j][k], dp[i][j+1][k], dp[i][j][k+1])
    return dp[0][0][0]