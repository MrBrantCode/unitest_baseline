"""
QUESTION:
Write a function `longestCommonSubstring` that takes two input strings `s` and `t` and returns the length of the longest common substring that starts and ends with the same character. The function should be able to handle any valid input strings.
"""

def longestCommonSubstring(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if s[i - 1] == s[0] and s[i - 1] == t[0]:
                    max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0
    return max_length