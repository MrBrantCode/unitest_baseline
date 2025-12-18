"""
QUESTION:
Write a function `minInsertions` that takes a string `s` of lowercase English letters as input, where the length of `s` is between 1 and 500, and returns the minimum number of character insertions required to transform `s` into a palindrome.
"""

def minInsertions(s):
    n = len(s)
    reverse_s = s[::-1]
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s[i-1] == reverse_s[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return n - dp[n][n]