"""
QUESTION:
Write a function named `calculate_edit_distance` that takes two strings `str1` and `str2` as input and returns the edit distance between them, considering only insertions, deletions, and substitutions. The function should have a time complexity of O(n^2), where n is the length of the longer string.
"""

def calculate_edit_distance(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    # Create a 2D array and initialize the first row and column
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(n1 + 1):
        dp[i][0] = i
    for j in range(n2 + 1):
        dp[0][j] = j

    # Fill in the rest of the array
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

    return dp[n1][n2]