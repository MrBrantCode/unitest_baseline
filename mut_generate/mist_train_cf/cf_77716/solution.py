"""
QUESTION:
Create a function named `identity_matrix` that generates an 'n x n' identity matrix and its sparse representation. The function should take an integer `n` as input and return a 2D list or list of lists representing the 'n x n' identity matrix. Additionally, it should also return a list of lists where each sublist contains the row index, column index, and value of non-zero elements in the identity matrix.
"""

def entrance(n):
    identity = [[1 if i==j else 0 for j in range(n)] for i in range(n)]
    sparse_representation = [[i, j, identity[i][j]] for i in range(n) for j in range(n) if identity[i][j] != 0]
    return identity, sparse_representation