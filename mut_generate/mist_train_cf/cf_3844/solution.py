"""
QUESTION:
Write a function `levenshteinDistance(s1, s2)` that calculates the Levenshtein distance between two input strings `s1` and `s2` using dynamic programming with a time complexity of O(m*n), where m and n are the lengths of `s1` and `s2`, respectively, without using any built-in string manipulation functions or libraries. The function should return the Levenshtein distance between `s1` and `s2`.
"""

def levenshteinDistance(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create a matrix of size (m+1) x (n+1) to store the distances
    dp = [[0] * (n+1) for _ in range(m+1)]

    # Initialize the first row and first column of the matrix
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    # Compute the distances for each substring
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]