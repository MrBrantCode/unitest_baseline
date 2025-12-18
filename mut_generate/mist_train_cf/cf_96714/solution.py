"""
QUESTION:
Given two strings of lowercase letters, write a function `min_operations(str1, str2)` to find the minimum cost to transform `str1` into `str2` using the operations of insertion, deletion, and replacement, where the cost of each operation is equal to the ASCII value of the character involved.
"""

def min_operations(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Create the matrix
    matrix = [[0] * (n+1) for _ in range(m+1)]
    
    # Fill in the matrix
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 and j == 0:
                matrix[i][j] = 0
            elif i == 0:
                matrix[i][j] = j * ord(str2[j-1])
            elif j == 0:
                matrix[i][j] = i * ord(str1[i-1])
            elif str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j-1] + ord(str2[j-1]), matrix[i-1][j] + ord(str1[i-1]), matrix[i][j-1] + ord(str2[j-1]))
    
    # Return the minimum cost
    return matrix[m][n]