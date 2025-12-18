"""
QUESTION:
Write a function `longestPalindromicSubstr` that finds the length of the longest palindromic substring of a given input string. The input is a string of characters and the function should return an integer representing the length of the longest palindromic substring.
"""

def longestPalindromicSubstr(s: str) -> int:
    n = len(s)
    max_len = 1
    dp = [[False] * n for _ in range(n)]

    # All characters of length 1 are palindrome
    for i in range(n):
        dp[i][i] = True

    # Check for substring of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_len = 2

    # Check for lengths greater than 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > max_len:
                    max_len = k

    return max_len