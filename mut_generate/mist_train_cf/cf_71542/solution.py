"""
QUESTION:
Write a function `longest_palindrome_subseq(s)` that returns the length of the longest palindromic subsequence in a given string `s`. The string `s` is composed solely of digits and English alphabets (either lower-case, upper-case, or both) and its length is between 1 and 1000 inclusive. In case of multiple valid solutions, any one of them can be returned.
"""

def longest_palindrome_subseq(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    return dp[0][n - 1]