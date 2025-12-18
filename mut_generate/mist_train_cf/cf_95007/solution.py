"""
QUESTION:
Given two strings str1 and str2, implement a function `edit_distance` that calculates the edit distance between them, defined as the minimum number of operations (insertions, deletions, and substitutions) required to transform str1 into str2. The function should have a time complexity of O(n^2), where n is the length of the longer string. 

The function should return the edit distance between the two strings, where the edit distance between two empty strings is 0, and the edit distance between a non-empty string and an empty string is equal to the length of the non-empty string. It can be assumed that the inputs are valid strings consisting only of lowercase letters.
"""

def edit_distance(str1: str, str2: str) -> int:
    m = len(str1)
    n = len(str2)

    # Create matrix
    dp = [[0] * (n+1) for _ in range(m+1)]

    # Initialize matrix
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    # Fill in matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    # Return edit distance
    return dp[m][n]