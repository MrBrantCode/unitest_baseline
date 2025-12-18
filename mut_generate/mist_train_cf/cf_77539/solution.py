"""
QUESTION:
Write a function `max_substring_length(s, t)` that determines the maximal length of the identical non-overlapping substring sequence shared by two input strings `s` and `t`. The strings may contain lowercase and uppercase letters, numbers, and special characters. The function should return the maximum length of the identical non-overlapping substring sequence.
"""

def max_substring_length(s, t):
    m = len(s)
    n = len(t)
    dp = [[0]* (n+1) for _ in range(m+1)]
    max_length = 0

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0
                
    return max_length