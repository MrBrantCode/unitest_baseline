"""
QUESTION:
Create a function `multiply_matrices` that takes two 2D lists `matrix1` and `matrix2` as input. The function should return the result of the matrix multiplication of `matrix1` and `matrix2`. If the matrices cannot be multiplied due to incompatible dimensions, the function should return without a result. The input matrices are valid (i.e., they are rectangular and contain only numbers) but their dimensions may not be compatible for multiplication.
"""

def multiply_matrices(matrix1, matrix2):
    # Get the dimensions of the matrices
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    # Check if the matrices can be multiplied
    if cols1 != rows2:
        print("Cannot multiply matrices. Invalid dimensions.")
        return
    
    # Create a result matrix with dimensions rows1 x cols2
    result = [[0] * cols2 for _ in range(rows1)]
    
    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result