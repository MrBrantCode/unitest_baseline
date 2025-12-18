"""
QUESTION:
Write a function `longest_palindrome_length(s)` that takes a string `s` as input and returns the length of the longest palindromic subsequence in `s`. The function should not use any built-in string manipulation functions. The input string `s` contains only lowercase letters.
"""

def longest_palindrome_length(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]