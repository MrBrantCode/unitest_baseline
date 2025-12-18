"""
QUESTION:
Write a function `find_max(matrix)` that calculates the maximum element in a given 2D matrix. The function should work with any size of matrix.
"""

def find_max(matrix):
    max_value = float('-inf') 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
    return max_value