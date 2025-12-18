"""
QUESTION:
Implement a function named `multiply_matrix_recursive` that multiplies two input matrices using Strassen's algorithm for efficient matrix multiplication. The function should handle square matrices of any size that are powers of 2 (e.g., 2x2, 4x4, 8x8, etc.) and should not use any libraries or built-in matrix multiplication functions. The input matrices will be represented as 2D lists of integers.
"""

def multiply_matrix_recursive(a, b):
    n = len(a)

    # Base case for recursion - when the matrix size is 1x1
    if n == 1:
        return [[a[0][0] * b[0][0]]]

    # Splitting the matrices into smaller sub-matrices
    mid = n // 2
    a11 = [row[:mid] for row in a[:mid]]
    a12 = [row[mid:] for row in a[:mid]]
    a21 = [row[:mid] for row in a[mid:]]
    a22 = [row[mid:] for row in a[mid:]]

    b11 = [row[:mid] for row in b[:mid]]
    b12 = [row[mid:] for row in b[:mid]]
    b21 = [row[:mid] for row in b[mid:]]
    b22 = [row[mid:] for row in b[mid:]]

    # Recursive multiplication of sub-matrices
    m1 = multiply_matrix_recursive(add_matrices(a11, a22), add_matrices(b11, b22))
    m2 = multiply_matrix_recursive(add_matrices(a21, a22), b11)
    m3 = multiply_matrix_recursive(a11, subtract_matrices(b12, b22))
    m4 = multiply_matrix_recursive(a22, subtract_matrices(b21, b11))
    m5 = multiply_matrix_recursive(add_matrices(a11, a12), b22)
    m6 = multiply_matrix_recursive(subtract_matrices(a21, a11), add_matrices(b11, b12))
    m7 = multiply_matrix_recursive(subtract_matrices(a12, a22), add_matrices(b21, b22))

    # Calculating the resulting sub-matrices
    c11 = subtract_matrices(add_matrices(add_matrices(m1, m4), m7), m5)
    c12 = add_matrices(m3, m5)
    c21 = add_matrices(m2, m4)
    c22 = subtract_matrices(add_matrices(add_matrices(m1, m3), m6), m2)

    # Combining the sub-matrices to form the final matrix
    result = []
    for i in range(mid):
        result.append(c11[i] + c12[i])
    for i in range(mid):
        result.append(c21[i] + c22[i])

    return result


def add_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[i]))] for i in range(len(a))]


def subtract_matrices(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[i]))] for i in range(len(a))]