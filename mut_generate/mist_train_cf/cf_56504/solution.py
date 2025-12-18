"""
QUESTION:
Write a function `matrix_power(matrix, power)` that takes a square matrix and a non-negative integer power as input, and returns the result of raising the matrix to that power. The function should use fast powering by squaring and handle potential integer overflow using a modulus value (10^9 + 7).
"""

def matrix_power(matrix, power):
    def mat_multiply(A, B, mod):
        result = [[0 for x in range(len(B[0]))] for y in range(len(A))]

        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
                    result[i][j] %= mod

        return result

    base = matrix
    result = [[(x == y) for x in range(len(matrix))] for y in range(len(matrix))]

    while power > 0:
        if power & 1:
            result = mat_multiply(result, base, 10 ** 9 + 7)
        base = mat_multiply(base, base, 10 ** 9 + 7)
        power >>= 1

    return result