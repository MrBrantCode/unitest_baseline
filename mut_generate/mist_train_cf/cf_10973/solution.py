"""
QUESTION:
Create a function called `multiply_matrices` that takes two 2D lists (matrices) as input and returns their product. The function should first check if the number of columns in the first matrix matches the number of rows in the second matrix. If not, it should return an error message. The matrices are assumed to be lists of lists where each inner list represents a row in the matrix and each element in the inner list represents an element in the row. The function should handle matrices with any number of rows and columns, as long as the multiplication is valid.
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