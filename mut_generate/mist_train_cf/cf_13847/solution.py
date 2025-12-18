"""
QUESTION:
Write a function `longestPalindrome` that takes a string `s` as input and returns the length of the longest palindromic substring within the given string. The input string only contains lowercase English letters. The function should be efficient and scalable for large inputs.
"""

def longestPalindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    max_length = 0
    
    for i in range(n):
        dp[i][i] = True
        max_length = 1
        
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                if j - i == 1 or dp[i+1][j-1]:
                    dp[i][j] = True
                    max_length = max(max_length, j - i + 1)
                    
    return max_length