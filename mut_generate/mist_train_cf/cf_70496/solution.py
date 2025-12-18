"""
QUESTION:
Given a string `s`, write a function `longestPalindromicSubsequence(s)` that returns the longest palindromic subsequence in `s`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. If there are multiple solutions, return any of them. The length of `s` is between 1 and 1000, and `s` consists of only digits and English letters (lower-case and/or upper-case).
"""

def longestPalindromicSubsequence(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    ans = ""
    
    for i in range(n):
        dp[i][i] = 1
        ans = s[i]
    
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
            ans = s[i:i+2]
    
    for start in range(n-1, -1, -1):
        for end in range(start+2, n):
            if s[start] == s[end]:
                dp[start][end] = dp[start + 1][end - 1] 
            else:
                dp[start][end] = max(dp[start+1][end], dp[start][end-1]) 
            
            if dp[start][end] > len(ans):
                ans = s[start:end+1]
                
    return ans