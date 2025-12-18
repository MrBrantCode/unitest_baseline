"""
QUESTION:
Write a function `add_matrices(mat1, mat2)` that takes two matrices of the same dimensions as input and returns their sum. The function should be able to handle matrices of any size, but it does not need to check if the input matrices have the same dimensions.
"""

def entrance(mat1, mat2):
    result = [[mat1[i][j] + mat2[i][j]  for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return result