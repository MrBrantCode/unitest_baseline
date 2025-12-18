"""
QUESTION:
Write a function `matrix_multiplication(A, B)` that takes two matrices A and B as input where the number of columns in A is equal to the number of rows in B. The function should perform matrix multiplication and return the resulting matrix. The input matrices A and B are represented as lists of lists where each inner list represents a row in the matrix, and each element in the inner list represents an element in the matrix. The function should return the resulting matrix in the same format. 

Function signature: `def matrix_multiplication(A: List[List[int]], B: List[List[int]]) -> List[List[int]]`
"""

from typing import List

def entance(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    m = len(A)
    n = len(B[0])
    p = len(B)
    
    C = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    
    return C