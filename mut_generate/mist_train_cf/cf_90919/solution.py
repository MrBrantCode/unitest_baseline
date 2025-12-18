"""
QUESTION:
Create a function `matrix_multiply(matrixA: List[List[int]], matrixB: List[List[int]]) -> List[List[int]]` that multiplies two matrices with different dimensions but compatible for multiplication. The function should return the resulting matrix. The matrices can only contain integers and the input is guaranteed to be valid, except when the number of columns in `matrixA` does not match the number of rows in `matrixB`, in which case the function should return an error message.
"""

from typing import List

def matrix_multiply(matrixA: List[List[int]], matrixB: List[List[int]]) -> List[List[int]]:
    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    rowsB = len(matrixB)
    colsB = len(matrixB[0])
    
    # Check if the matrices can be multiplied
    if colsA != rowsB:
        return "The matrices cannot be multiplied"
    
    # Create an empty matrix to store the result
    result = [[0 for _ in range(colsB)] for _ in range(rowsA)]
    
    # Perform the multiplication
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
    
    return result