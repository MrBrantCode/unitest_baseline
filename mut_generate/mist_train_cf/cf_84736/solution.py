"""
QUESTION:
Write a function `check_inc_matrix` that takes a bi-dimensional list (matrix) as an argument and returns True if all rows and columns in the matrix strictly increment, and False otherwise. The function should check both horizontal and vertical sequences, ensuring that each element is strictly less than its succeeding element.
"""

def check_inc_matrix(matrix):
    # Checking horizontal sequence
    for row in matrix:
        for i in range(len(row) - 1):
            if row[i] >= row[i+1]:
                return False
    
    # Checking vertical sequence
    for col in range(len(matrix[0])):
        for row in range(len(matrix)-1):
            if matrix[row][col] >= matrix[row+1][col]:
                return False             

    return True