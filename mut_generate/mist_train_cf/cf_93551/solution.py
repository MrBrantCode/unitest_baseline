"""
QUESTION:
Write a function called `reverse_matrix` that takes a matrix of numbers as input and returns a new matrix with the order of rows and columns reversed. The input matrix will have at least 2 rows and 2 columns, and the function should handle matrices of any size, including non-square matrices where the number of rows and columns can be different.
"""

def reverse_matrix(matrix):
    new_matrix = []
    for j in range(len(matrix[0])):  
        new_row = []
        for i in range(len(matrix)):  
            new_row.append(matrix[i][j])
        new_matrix.append(new_row)
    return new_matrix