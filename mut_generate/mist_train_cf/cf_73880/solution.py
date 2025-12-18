"""
QUESTION:
Write a function `find_char(matrix, c)` that finds the one-dimensional index pair (i,j) of the first occurrence of a character 'c' in a given matrix of n*m size where each cell contains a string of a single character. The function should return a tuple (i, j) representing the row and column index of the character 'c' in the matrix, with 0-indexed based on Python list indexing conventions, and should not exceed O(n*m) time complexity.
"""

def find_char(matrix, c):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == c:
                return (i, j)
    return None