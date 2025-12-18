"""
QUESTION:
Implement a function `longest_palindrome(s: str) -> int` that finds the length of the longest palindrome substring in a given string. The input string `s` has a length between 1 and 1000 (inclusive). Return the length of the longest palindrome substring.
"""

def longest_palindrome(s: str) -> int:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    max_length = 1

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_length = 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                max_length = max(max_length, length)

    return max_length