"""
QUESTION:
Implement a function named `damerau_levenshtein_distance` that calculates the Damerau-Levenshtein Distance between two input strings `str1` and `str2`. The function should have a time complexity of O(m*n), where m and n are the lengths of `str1` and `str2`, respectively. The Damerau-Levenshtein Distance allows for four types of operations: insertion, deletion, substitution, and transposition, where transposition is defined as swapping two adjacent characters in a string.
"""

def damerau_levenshtein_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Initialize the matrix with zeros
    dist = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and column
    for i in range(m + 1):
        dist[i][0] = i
    for j in range(n + 1):
        dist[0][j] = j
    
    # Fill in the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
            
            # Calculate the minimum of the three adjacent cells (insertion, deletion, substitution)
            dist[i][j] = min(dist[i - 1][j] + 1,        # deletion
                             dist[i][j - 1] + 1,        # insertion
                             dist[i - 1][j - 1] + cost)  # substitution
            
            # Check for transposition
            if i > 1 and j > 1 and str1[i - 1] == str2[j - 2] and str1[i - 2] == str2[j - 1]:
                dist[i][j] = min(dist[i][j], dist[i - 2][j - 2] + cost)  # transposition
    
    return dist[m][n]