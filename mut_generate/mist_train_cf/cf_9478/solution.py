"""
QUESTION:
Create a function `matrix_multiply(matrixA, matrixB)` that takes two input matrices with compatible dimensions for multiplication and returns the resulting matrix. The function should assume that the input matrices can have different dimensions but are always compatible for multiplication.
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