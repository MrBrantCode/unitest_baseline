"""
QUESTION:
Create a function `sum_neighbors(matrix)` that takes a 2D array (MxN matrix) as input and returns a new matrix where each element is the sum of the corresponding element in the original matrix and its neighboring elements (top, bottom, left, right).
"""

def sum_neighbors(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            total = matrix[i][j]
            
            if i > 0:  
                total += matrix[i - 1][j]
            if i < rows - 1:  
                total += matrix[i + 1][j]
            if j > 0:  
                total += matrix[i][j - 1]
            if j < cols - 1:  
                total += matrix[i][j + 1]

            new_matrix[i][j] = total

    return new_matrix