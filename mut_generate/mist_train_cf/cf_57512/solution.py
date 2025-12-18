"""
QUESTION:
Given a string s consisting of lowercase English letters with a length not larger than 20,100, write a function `palindromic_substrings(s)` that finds all the start and end indices of s's palindromic substrings. The order of output does not matter.
"""

def palindromic_substrings(s):
    if not s:
        return []
    dp = [[False]*len(s) for _ in range(len(s))]
    res = []
    for i in range(len(s)-1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                dp[i][j] = True
                res.append([i, j])
    return res