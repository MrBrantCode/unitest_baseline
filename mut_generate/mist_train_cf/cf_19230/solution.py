"""
QUESTION:
Write a function called `levenshtein_distance` that takes two strings `str1` and `str2` as input and returns the minimum number of single-character edits (insertions, deletions, or substitutions) required to change `str1` into `str2`. The function should not assume that the two input strings have the same length.
"""

def levenshtein_distance(str1, str2):
    """
    Calculate the minimum number of single-character edits (insertions, deletions, or substitutions) 
    required to change str1 into str2.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        int: The Levenshtein distance between str1 and str2.
    """
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