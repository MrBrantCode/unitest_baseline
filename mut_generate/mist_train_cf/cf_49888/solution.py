"""
QUESTION:
Write a function called `longest_common_palindromic_subsequence` that takes two strings, `string1` and `string2`, as input and returns the length of their longest common palindromic subsequence. The function should be case sensitive, treating 'a' and 'A' as different characters. The solution should have an optimized time complexity.
"""

def longest_common_palindromic_subsequence(string1, string2):
    def lcs(X, Y, m, n):
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

    n, m = len(string1), len(string2)
    rev_string2 = string2[::-1]
    len_lps = lcs(string1, rev_string2, n, m)
    return len_lps