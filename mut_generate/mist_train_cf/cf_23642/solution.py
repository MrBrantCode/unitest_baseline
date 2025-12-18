"""
QUESTION:
Write a function `transpose_matrix(matrix)` that takes a 2D list `matrix` as input and returns its transpose. The input matrix can be of any size m x n. The function should return a new 2D list where the rows of the original matrix are now the columns and vice versa.
"""

def transpose_matrix(matrix):
    t_matrix = []
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        t_matrix.append(temp)
    return t_matrix