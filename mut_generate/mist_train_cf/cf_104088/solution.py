"""
QUESTION:
Write a function `multiply_matrices` that takes two matrices `matrix1` and `matrix2` as input and returns their product. The function should first check if the number of columns in `matrix1` is equal to the number of rows in `matrix2`. If they are not equal, the function should return an error message "Matrices cannot be multiplied". Otherwise, it should return the resulting matrix of the multiplication. Assume that the input matrices are valid (i.e., all rows have the same number of elements). The resulting matrix should have dimensions (rows of `matrix1`, columns of `matrix2`).
"""

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    # Get dimensions of matrices
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    # Check if matrices can be multiplied
    if cols1 != rows2:
        return "Matrices cannot be multiplied"
    
    # Initialize resulting matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    # Multiply matrices
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result