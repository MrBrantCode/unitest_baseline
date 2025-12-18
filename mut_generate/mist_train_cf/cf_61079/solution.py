"""
QUESTION:
Write a function `mul_mat` that multiplies two given matrices A and B without using any external libraries. The function should first check if the number of columns in matrix A is equal to the number of rows in matrix B, and if not, return an error message. If the matrices are compatible for multiplication, perform the multiplication and return the resulting matrix. Additionally, write a function `transpose` to find the transpose of the resulting matrix.
"""

def mul_mat(A, B):
    """Multiplies two matrices A and B."""
    rows_mat1 = len(A)
    cols_mat1 = len(A[0])
    rows_mat2 = len(B)
    cols_mat2 = len(B[0])
    
    if cols_mat1 != rows_mat2:
        return "Error! Matrix dimensions are not compatible for multiplication."
    
    # Initialize result matrix filled with zeros
    res = [[0 for _ in range(cols_mat2)] for _ in range(rows_mat1)]
    
    # Multiply mat1 and mat2 and store in res
    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(cols_mat1):  # or for k in range(rows_mat2)
                res[i][j] += A[i][k] * B[k][j]
    return res

def transpose(mat):
    """Finds the transpose of a given matrix."""
    rows = len(mat)
    cols = len(mat[0])
    
    # Initialize transpose matrix filled with zeros
    t = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Store transpose of mat in t
    for i in range(rows):
        for j in range(cols):
            t[j][i] = mat[i][j]
    return t