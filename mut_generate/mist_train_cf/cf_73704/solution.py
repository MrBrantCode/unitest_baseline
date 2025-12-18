"""
QUESTION:
Create a function `multiply_matrices` that takes two input matrices `mat1` and `mat2` and returns their product if the number of columns in `mat1` is equal to the number of rows in `mat2`, otherwise return an error message. The function should handle empty input matrices.
"""

def multiply_matrices(mat1, mat2):
    # Number of rows in mat1
    r1 = len(mat1)
    # Number of columns in mat1
    c1 = len(mat1[0]) if mat1 else 0
    # Number of rows in mat2
    r2 = len(mat2)
    # Number of columns in mat2
    c2 = len(mat2[0]) if mat2 else 0

    # Check if multiplication is possible
    if c1 != r2:
        print("Matrices cannot be multiplied")
        return

    # Create the result matrix and initialize it to 0
    product = [[0 for col in range(c2)] for row in range(r1)]

    # Execute matrix multiplication
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):  # also equal to r2
                product[i][j] += mat1[i][k] * mat2[k][j]

    return product