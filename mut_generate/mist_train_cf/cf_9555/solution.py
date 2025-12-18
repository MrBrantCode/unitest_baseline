"""
QUESTION:
Construct a function named `longest_common_subsequence` that takes two string parameters, `s1` and `s2`, and returns the length of the longest common subsequence between the two strings along with the actual subsequence itself. The function should not have any restrictions on the characters in the strings, but it should return a subsequence that can be derived from the original strings by deleting some or no elements without changing the order of the remaining elements. The subsequence does not have to be continuous.
"""

def longest_common_subsequence(s1, s2):
    m = len(s1)
    n = len(s2)
    
    # Create a matrix with dimensions (m+1) x (n+1)
    matrix = [[0] * (n+1) for _ in range(m+1)]
    
    # Fill the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    
    # Reconstruct the longest common subsequence
    subsequence = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            subsequence = s1[i-1] + subsequence
            i -= 1
            j -= 1
        elif matrix[i-1][j] > matrix[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return matrix[m][n], subsequence