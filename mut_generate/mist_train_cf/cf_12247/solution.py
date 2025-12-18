"""
QUESTION:
Write a function minEditDistance(str1, str2) that takes two strings str1 and str2 as input and returns the minimum number of operations (insertions, deletions, or substitutions) required to change str1 into str2.
"""

def minEditDistance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a matrix of size (m+1) x (n+1)
    dp = [[0] * (n+1) for _ in range(m+1)]

    # Fill in the base cases
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

    return dp[m][n]