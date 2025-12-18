"""
QUESTION:
Create a function named `arrayToMatrix` that takes a one-dimensional list of integers as input and returns a square matrix. The function should arrange the input list into a square matrix with equal number of rows and columns, assuming the length of the list is a perfect square.
"""

def arrayToMatrix(array):
    n = int(len(array)**0.5)
    matrix = []
 
    for i in range(n):
        matrix.append(array[i*n:(i+1)*n])
 
    return matrix