"""
QUESTION:
Write a function `calc_det(matrix)` to calculate the determinant of a given square matrix. The input matrix is a list of lists where each inner list has the same length, representing a square matrix. The size of the matrix is 2x2 or larger. The function should return the determinant of the matrix.
"""

def calc_det(matrix):
    #Get length(size) of the matrix
    size = len(matrix)

    #If the matrix is 2x2, calculate and return the determinant
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    #Initiate determinant as 0
    determinant = 0

    #If the matrix is not 2x2, recursively calculate the determinant
    for i in range(size):
        submatrix = [] #Create submatrix
        for j in range(1, size):
            row = []
            for k in range(size):
                if k != i:
                    row.append(matrix[j][k])
            submatrix.append(row)
        #recursively calculate the determinant
        determinant += ((-1) ** i) * matrix[0][i] * calc_det(submatrix)
    return determinant