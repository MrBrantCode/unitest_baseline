"""
QUESTION:
Write a function `perform_operations(x, y)` that takes two 1-dimensional NumPy arrays `x` and `y` of the same length as input. The function should perform the following operations: 
1. Reshape `x` and `y` to have a new axis using `np.newaxis`. 
2. Construct a matrix `D` by horizontally stacking arrays `x*x`, `x*y`, `y*y`, `x`, `y`, and an array of ones. 
3. Calculate the dot product of the transpose of matrix `D` with itself and store the result in matrix `S`. 
4. Initialize a 6x6 matrix `C` with zeros and set `C[0,2]`, `C[2,0]`, and `C[1,1]` to 2, 2, and -1 respectively. 
5. Calculate the eigenvalues and eigenvectors of the matrix product of the inverse of `S` and `C`. The function should return the calculated eigenvalues and eigenvectors.
"""

import numpy as np

def perform_operations(x, y):
    x = x[:,np.newaxis]
    y = y[:,np.newaxis]
    D =  np.hstack((x*x, x*y, y*y, x, y, np.ones_like(x)))
    S = np.dot(D.T,D)
    C = np.zeros([6,6])
    C[0,2] = C[2,0] = 2
    C[1,1] = -1
    E, V = np.linalg.eig(np.dot(np.linalg.inv(S), C))
    return E, V