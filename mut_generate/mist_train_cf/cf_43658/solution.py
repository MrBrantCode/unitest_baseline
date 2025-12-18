"""
QUESTION:
Write a function `longest_common_subsequence(text1, text2)` that takes two strings `text1` and `text2` consisting of only lowercase English letters from "a"-"z" with lengths between 1 and 1000, and returns the length of their longest common subsequence and the subsequence itself. If there is no common subsequence, return 0 and an empty string.
"""

def longest_common_subsequence(text1, text2):
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    lcs = []

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = len(text1), len(text2)
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[-1][-1], "".join(reversed(lcs))