"""
QUESTION:
Implement a function `countPS(s)` that takes a string `s` as input and returns the count of all unique palindromic sub-sequences in the string. The function should use dynamic programming and consider a sub-sequence as palindromic if it reads the same backward as forward, regardless of the order of characters in between.
"""

def countPS(s):
    n = len(s)
    dp = [[0 for _ in range(n+1)]for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][i] = 1

    for cl in range(2, n+1):
        for i in range(n):
            k = cl + i - 1
            if k >= n:
                break
            if s[i] == s[k]:
                dp[i][k] = dp[i][k-1] + dp[i+1][k] + 1
            else:
                dp[i][k] = dp[i][k-1] + dp[i+1][k] - dp[i+1][k-1]

    return dp[0][n-1]