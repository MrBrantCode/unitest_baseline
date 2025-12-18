"""
QUESTION:
Write a function named `perspective_projection_matrix` that takes a 1D list of 16 floating-point numbers representing the elements of a 4x4 matrix in row-major order. The function should return a 2D list representing the corresponding 4x4 matrix. The input list will always contain 16 elements.
"""

from typing import List

def entrance(arr: List[float]) -> List[List[float]]:
    matrix = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            matrix[i][j] = arr[i*4 + j]
    return matrix