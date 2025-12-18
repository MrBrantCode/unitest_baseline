"""
QUESTION:
Write a function `findPalindromicSubstrings(s)` that takes a string `s` as input and returns all unique palindromic substrings in the original order of their appearance. The function should consider all possible substrings, including those with a length of 1 and 2 characters.
"""

def findPalindromicSubstrings(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    result = []
    
    for i in range(n):
        dp[i][i] = True
        result.append(s[i])
    
    for j in range(1, n):
        for i in range(j):
            if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                dp[i][j] = True
                result.append(s[i:j+1])
    
    return result