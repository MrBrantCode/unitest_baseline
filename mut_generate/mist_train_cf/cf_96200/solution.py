"""
QUESTION:
Create a function `fibonacci(N)` that calculates the Nth Fibonacci number, where N is a positive integer less than or equal to 10^9. The function should have a time complexity of O(logN) and a space complexity of O(1).
"""

def fibonacci(N):
    if N == 0 or N == 1:
        return N

    A = [[1, 1], [1, 0]]
    B = matrix_power(A, N-1)
    return B[0][0]

def matrix_power(A, N):
    if N == 0:
        return [[1, 0], [0, 1]]
    
    if N % 2 == 1:
        return matrix_multiply(matrix_power(A, N-1), A)
    
    B = matrix_power(matrix_multiply(A, A), N//2)
    return B

def matrix_multiply(X, Y):
    return [[(X[0][0] * Y[0][0]) + (X[0][1] * Y[1][0]), (X[0][0] * Y[0][1]) + (X[0][1] * Y[1][1])],
            [(X[1][0] * Y[0][0]) + (X[1][1] * Y[1][0]), (X[1][0] * Y[0][1]) + (X[1][1] * Y[1][1])]]