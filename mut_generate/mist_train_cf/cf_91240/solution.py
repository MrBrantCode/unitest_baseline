"""
QUESTION:
Write a function `levenshtein_distance(word1, word2)` that calculates the minimum number of single-character edits (insertions, deletions, or substitutions) required to transform `word1` into `word2`. The function should return the edit distance between the two input words.
"""

def levenshtein_distance(word1, word2):
    m = len(word1)
    n = len(word2)
    
    # Create a distance matrix
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Initialize the first row and column of the matrix
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    
    # Fill in the rest of the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    # Return the minimum number of edits required
    return dp[m][n]