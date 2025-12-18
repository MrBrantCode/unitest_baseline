"""
QUESTION:
Write a function `longest_common_substring(x, y)` that takes in two strings `x` and `y` and returns the length of the longest common substring between them, where a substring is a contiguous sequence of characters within a string.
"""

def longest_common_substring(x, y):
    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])

    return max_length