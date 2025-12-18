"""
QUESTION:
Implement a function `levenshtein_distance(str1, str2)` that calculates the minimum number of single-character edits (insertions, deletions, or substitutions) required to change `str1` into `str2`. The function should take two strings `str1` and `str2` as input and return the Levenshtein distance between them.
"""

def levenshtein_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D matrix with (m+1) rows and (n+1) columns
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Calculate the distance for each cell in the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

    # Return the bottom-right cell of the matrix
    return dp[m][n]