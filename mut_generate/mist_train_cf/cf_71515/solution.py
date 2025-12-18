"""
QUESTION:
Create a function named `longestPalindrome` that takes a string `s` as input and returns the length of the longest palindromic substring in `s`. The function should consider all possible substrings of `s` and determine the maximum length of a palindromic substring.
"""

def longestPalindrome(s):
    str_length = len(s)
    dp = [[False]*str_length for _ in range(str_length)]
    max_length = 0

    for i in range(str_length):
        dp[i][i] = True
        max_length = 1

    for i in range(str_length - 1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            max_length = 2

    for length in range(3, str_length+1):
        for i in range(str_length - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1] == True:
                dp[i][j] = True
                max_length = length
    return max_length