"""
QUESTION:
Create a function `get_even_elements(matrix, row_wise=True)` that takes a 2D matrix and a boolean flag `row_wise` as input. The function should return a generator expression that iterates over the matrix in a row-wise manner if `row_wise` is `True` and column-wise manner if `row_wise` is `False`, yielding only the even elements. The matrix can have a variable number of rows and columns.
"""

def get_even_elements(matrix, row_wise=True):
    if row_wise:
        return (elem for row in matrix for elem in row if elem % 2 == 0)
    else:  
        transposed_matrix = zip(*matrix)  # transpose matrix for column-wise iteration
        return (elem for column in transposed_matrix for elem in column if elem % 2 == 0)