"""
QUESTION:
Design a function `longest_palindrome_subsequence(s)` that takes a string `s` as input and returns the length of the longest palindromic subsequence in `s`. The function should have a time complexity of O(n^2) where n is the length of `s`.
"""

def longest_palindrome_subsequence(s):
    length = len(s)

    # Create a square matrix. Initialize all values as 0.
    dp = [[0] * length for _ in range(length)]

    # All letters are palindromes of length 1
    for i in range(length):
        dp[i][i] = 1

    for cl in range(2, length+1):
        for i in range(length - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])

    return dp[0][length-1]