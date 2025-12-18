"""
QUESTION:
Design a function `multiply_individual_elements(matrix)` that takes a 2D list of numbers as input and returns a new 2D list where each element is the square of the corresponding element in the input matrix. Assume all elements in the matrix are numeric and all rows have the same length.
"""

def multiply_individual_elements(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix[i][j] * matrix[i][j]
    
    return result