"""
QUESTION:
Create a function `longest_common_substring(s1, s2)` that finds the longest common substring from two given strings `s1` and `s2`. The function should have a time complexity of O(n^2), where n is the length of the longer string. It should handle cases where the strings can contain special characters and are case-sensitive. It should not use any built-in functions or libraries specifically designed for string manipulation.
"""

def longest_common_substring(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    maxLen = 0
    endIdx1 = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > maxLen:
                    maxLen = dp[i][j]
                    endIdx1 = i
            else:
                dp[i][j] = 0

    return s1[endIdx1 - maxLen: endIdx1]