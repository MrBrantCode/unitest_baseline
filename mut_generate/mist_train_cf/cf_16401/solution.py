"""
QUESTION:
Given two input strings s and t, implement a function longest_common_substring(s, t) to find the length of the longest common substring that starts and ends with the same character. The function should return the maximum length of such a substring.
"""

def entrance(s, t):
    m = len(s)
    n = len(t)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length and s[i - 1] == s[i - dp[i][j]]:
                    max_length = dp[i][j]
            else:
                dp[i][j] = 0

    return max_length