"""
QUESTION:
Write a function `levenshtein_distance` that calculates the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into another. The function should take two strings as input and return the Levenshtein distance between them. The function should not take any other parameters and should not use any external libraries or built-in functions that calculate the Levenshtein distance.
"""

def levenshtein_distance(s1, s2):
    """
    This function calculates the Levenshtein distance between two input strings.
    
    The Levenshtein distance is a measure of the minimum number of single-character edits (insertions, deletions or substitutions) 
    required to change one string into the other.
    
    Args:
    s1 (str): The first input string.
    s2 (str): The second input string.
    
    Returns:
    int: The Levenshtein distance between s1 and s2.
    """
    
    # Initialize a matrix to store the Levenshtein distances between substrings of s1 and s2
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the base cases
    # The Levenshtein distance between a string and an empty string is the length of the string
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill in the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If the current characters in s1 and s2 are the same, there's no edit needed
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # Otherwise, consider all possible edits and choose the one with the minimum cost
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    # The Levenshtein distance between s1 and s2 is stored in the bottom-right corner of the matrix
    return dp[m][n]