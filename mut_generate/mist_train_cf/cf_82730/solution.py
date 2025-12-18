"""
QUESTION:
Design a function `longest_palindromic_subsequence(s)` that takes a string `s` as input and returns a tuple containing the length of the longest palindromic subsequence and the count of such subsequences. The function should not use any external libraries or built-in functions that solve the problem directly, but it can use dynamic programming.
"""

def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    count = [[0] * n for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        count[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
                count[i][j] = count[i+1][j-1]
                if dp[i][j] == 2:
                    count[i][j] += 1
            else:
                if dp[i+1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i+1][j]
                    count[i][j] = count[i+1][j]
                elif dp[i+1][j] < dp[i][j-1]:
                    dp[i][j] = dp[i][j-1]
                    count[i][j] = count[i][j-1]
                else:
                    dp[i][j] = dp[i+1][j]
                    count[i][j] = count[i+1][j] + count[i][j-1]
                    if dp[i+1][j-1] > 0:
                        count[i][j] -= count[i+1][j-1]

    return dp[0][n-1], count[0][n-1]