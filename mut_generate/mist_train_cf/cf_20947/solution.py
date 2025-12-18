"""
QUESTION:
Write a function `levenshtein_distance(s1, s2)` that calculates the Levenshtein distance between two strings `s1` and `s2`. The Levenshtein distance is the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into another. The function should have a time complexity of less than O(n^3) and a space complexity of less than O(n^2), where n is the length of the longer string.
"""

def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    
    # Create a 2D array to store the Levenshtein distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Calculate the Levenshtein distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    
    # Return the final Levenshtein distance
    return dp[m][n]