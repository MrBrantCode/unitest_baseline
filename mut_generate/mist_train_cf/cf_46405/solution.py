"""
QUESTION:
Write a Python function `cube_matrix` that takes a 2D list `mat` as input, where each inner list represents a row of a matrix, and returns a new 2D list where each element of the original matrix is raised to the power of 3.
"""

def cube_matrix(mat):
    return [[ele**3 for ele in row] for row in mat]