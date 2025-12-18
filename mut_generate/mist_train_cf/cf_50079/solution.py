"""
QUESTION:
Implement a function `fibonacci(n)` that calculates the nth Fibonacci number using matrix exponentiation and memoization. The function should not use recursion or loops to calculate the Fibonacci sequence itself, but may use these methods for the matrix exponentiation and memoization. The input `n` is a non-negative integer and the output is the nth Fibonacci number.
"""

def fibonacci(n):
    if n <= 1:
        return n

    memo = {}
    matrix = [[1, 1], [1, 0]]

    def multiply_matrices(a, b):
        result = [[0, 0], [0, 0]]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
        return result

    def matrix_power(matrix, n, memo):
        if n == 1:
            return matrix
        elif n in memo:
            return memo[n]
        elif n%2 == 0:
            memo[n//2] = matrix_power(matrix, n//2, memo)
            return multiply_matrices(memo[n//2], memo[n//2])
        else:
            memo[n-1] = matrix_power(matrix, n-1, memo)
            return multiply_matrices(matrix, memo[n-1])

    result_matrix = matrix_power(matrix, n - 1, memo)
    return result_matrix[0][0]