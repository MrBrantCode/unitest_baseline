"""
QUESTION:
Implement a function named `levenshtein_distance` that calculates the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into another. The function should take two strings, `str1` and `str2`, as input and return the Levenshtein distance between them. Note that there are no restrictions on the lengths of `str1` and `str2`.
"""

def levenshtein_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    matrix = [[0] * (n+1) for _ in range(m+1)]
    
    for i in range(m+1):
        matrix[i][0] = i
    for j in range(n+1):
        matrix[0][j] = j
        
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                
    return matrix[m][n]