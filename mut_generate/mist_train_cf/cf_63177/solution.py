"""
QUESTION:
Write a function `max_common_substring(s, t)` that takes two strings `s` and `t` as input and returns the length of the longest common substring of `s` and `t`. The function should not return the substring itself, only its length.
"""

def max_common_substring(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]