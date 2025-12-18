"""
QUESTION:
Implement the `longest_palindrome` function which takes a string of lowercase alphabets (with a maximum length of 1000) as input and returns the length of the longest palindrome substring in the given string.

The function should be implemented as follows: `def longest_palindrome(s: str) -> int:`
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