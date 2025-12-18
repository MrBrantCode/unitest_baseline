"""
QUESTION:
Write a function named `maximum_sum` that takes two strings `s1` and `s2` as input, each containing only lowercase English letters (ASCII value between 97 and 122) and having a length between 1 and 1000. The function should return the maximum ASCII sum of retained characters that can be obtained by removing some characters from both strings to make them equal.
"""

def maximum_sum(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + ord(s1[i-1]) * 2)
            dp[i][j] = max(dp[i][j], max(dp[i-1][j], dp[i][j-1]))
        
    return dp[m][n]