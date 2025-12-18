"""
QUESTION:
Implement a function `fibonacci(n)` that generates the nth element in a Fibonacci series, where `n` is a positive integer. The function should have a time complexity of O(log n) and a space complexity of O(log n). Note that iteration or recursion is not allowed in the implementation, but the use of matrix exponentiation is acceptable.
"""

def fibonacci(n):
    def multiply_matrix(A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
        ]

    def power_matrix(A, n):
        if n == 0:
            return [[1, 0], [0, 1]]  

        if n % 2 == 0:
            sqrt = power_matrix(A, n // 2)
            return multiply_matrix(sqrt, sqrt)
        else:
            sqrt = power_matrix(A, (n - 1) // 2)
            return multiply_matrix(multiply_matrix(sqrt, sqrt), A)

    matrix = [[1, 1], [1, 0]]
    power = power_matrix(matrix, n)

    return power[1][0]  