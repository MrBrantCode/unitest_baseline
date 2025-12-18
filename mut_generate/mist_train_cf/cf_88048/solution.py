"""
QUESTION:
Implement the `matrix_multiply` function to perform matrix multiplication using Strassen's algorithm. The function should take two square matrices A and B as input and return their product. The time complexity should be less than O(n^3), where n is the size of the input matrices. The implementation should use recursion and handle square matrices of arbitrary size, assuming that the input matrices are always of compatible sizes for multiplication.
"""

def matrix_multiply(A, B):
    def split_matrix(M):
        n = len(M)
        half = n // 2
        upper_left = [row[:half] for row in M[:half]]
        upper_right = [row[half:] for row in M[:half]]
        lower_left = [row[:half] for row in M[half:]]
        lower_right = [row[half:] for row in M[half:]]
        return upper_left, upper_right, lower_left, lower_right

    def add_matrices(A, B):
        n = len(A)
        C = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                C[i][j] = A[i][j] + B[i][j]
        return C

    def subtract_matrices(A, B):
        n = len(A)
        C = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                C[i][j] = A[i][j] - B[i][j]
        return C

    def combine_matrices(upper_left, upper_right, lower_left, lower_right):
        n = len(upper_left)
        result = [[0] * (2 * n) for _ in range(2 * n)]
        for i in range(n):
            for j in range(n):
                result[i][j] = upper_left[i][j]
                result[i][j + n] = upper_right[i][j]
                result[i + n][j] = lower_left[i][j]
                result[i + n][j + n] = lower_right[i][j]
        return result

    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]

    a, b, c, d = split_matrix(A)
    e, f, g, h = split_matrix(B)

    p1 = matrix_multiply(a, subtract_matrices(f, h))
    p2 = matrix_multiply(add_matrices(a, b), h)
    p3 = matrix_multiply(add_matrices(c, d), e)
    p4 = matrix_multiply(d, subtract_matrices(g, e))
    p5 = matrix_multiply(add_matrices(a, d), add_matrices(e, h))
    p6 = matrix_multiply(subtract_matrices(b, d), add_matrices(g, h))
    p7 = matrix_multiply(subtract_matrices(a, c), add_matrices(e, f))

    q1 = add_matrices(subtract_matrices(add_matrices(p5, p4), p2), p6)
    q2 = add_matrices(p1, p2)
    q3 = add_matrices(p3, p4)
    q4 = subtract_matrices(subtract_matrices(add_matrices(p1, p5), p3), p7)

    result = combine_matrices(q1, q2, q3, q4)
    return result