"""
QUESTION:
Given two strings `word1` and `word2` composed of lowercase English letters, determine the maximum length of a palindrome that can be created by selecting a non-empty subsequence from `word1` and `word2` and concatenating them. If it's impossible to construct a palindrome, return `0`. 

The function should take two strings `word1` and `word2` as input and return an integer representing the maximum length of a palindrome. The lengths of `word1` and `word2` are between 1 and 1000 (inclusive).
"""

def longestPalindrome(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    max_len = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if word1[i-1]==word2[j-1]:
                if i==1 or j==1:
                    dp[i][j]=2
                else:
                    dp[i][j]=dp[i-1][j-1]+2
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            max_len = max(max_len, dp[i][j])
    return max_len