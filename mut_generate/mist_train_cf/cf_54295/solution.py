"""
QUESTION:
Create a function `spiralOrder(matrix)` that takes a 2D list of integers as input and returns a 1D list containing the elements from the input matrix in a spiraling, clockwise order. The input matrix can be of any size, and the function should process all elements from the matrix.
"""

def spiralOrder(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]  

    return res