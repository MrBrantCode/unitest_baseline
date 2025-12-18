"""
QUESTION:
Write a function named `fibonacci` that takes an integer `n` as input and returns the nth Fibonacci number. The function should have a time complexity of O(log n) and use dynamic programming with a constant amount of space.
"""

def fibonacci(n):
    def multiply_matrices(A, B):
        a, b, c = A[0][0], A[0][1], A[1][0]
        d, e, f = B[0][0], B[0][1], B[1][0]
        
        return [
            [a*d + b*e, a*e + b*f],
            [c*d + e*d, c*e + e*f]
        ]

    def power_matrix(A, n):
        if n == 0:
            return [[1, 0], [0, 1]]  # Identity matrix
        
        result = power_matrix(A, n // 2)
        result = multiply_matrices(result, result)
        
        if n % 2 == 1:
            result = multiply_matrices(result, A)
        
        return result
    
    if n == 0:
        return 0
    
    matrix = [[1, 1], [1, 0]]
    result = power_matrix(matrix, n - 1)
    
    return result[0][0]