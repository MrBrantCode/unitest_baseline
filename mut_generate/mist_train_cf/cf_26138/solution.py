"""
QUESTION:
Write a function `multiply(A, B)` that takes two 2D lists `A` and `B` as input, representing matrices, and returns their product. The function should check if the matrices can be multiplied based on their dimensions, and if not, it should print an error message and return without the result. The dimensions of the matrices are not fixed, but they should be compatible for matrix multiplication (i.e., the number of columns in `A` must be equal to the number of rows in `B`).
"""

def multiply(A, B): 
    rows_A = len(A) 
    cols_A = len(A[0]) 
    rows_B = len(B) 
    cols_B = len(B[0]) 
  
    if cols_A != rows_B: 
        print("Cannot multiply the two matrices. Incorrect dimensions.") 
        return  
    C = [[0 for row in range(cols_B)] for col in range(rows_A)] 
  
    for i in range(rows_A): 
        for j in range(cols_B): 
            for k in range(cols_A): 
                C[i][j] += A[i][k] * B[k][j] 
  
    return C