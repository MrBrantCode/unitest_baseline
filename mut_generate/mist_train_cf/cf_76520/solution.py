"""
QUESTION:
Create a function called `editDistance` that calculates the edit distance (or Levenshtein distance) between two strings. The function should take three parameters: two input strings and their lengths. The function should return the minimum number of operations (insertions, deletions, or substitutions) required to transform one string into another. The function should use dynamic programming.
"""

def editDistance(str1, str2, m, n):
    """
    Calculate the edit distance (or Levenshtein distance) between two strings.
    
    This function uses dynamic programming to calculate the minimum number of operations
    (insertions, deletions, or substitutions) required to transform one string into another.
    
    Parameters:
    str1 (str): The first input string.
    str2 (str): The second input string.
    m (int): The length of the first string.
    n (int): The length of the second string.
    
    Returns:
    int: The edit distance between the two strings.
    """
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])      # Replace 
    return dp[m][n]