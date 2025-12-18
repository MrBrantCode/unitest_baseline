"""
QUESTION:
Write a function `fibonacci(k)` that returns the kth element in the Fibonacci sequence with a time complexity of O(log n) and without using recursion. The function should handle invalid inputs where k is less than 0 and return a corresponding error message. For k values 0 and 1, the function should return k.
"""

def fibonacci(k):
    if k < 0:
        return "Invalid input"

    if k <= 1:
        return k

    # Helper function for matrix multiplication
    def multiply(a, b):
        x = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        y = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        z = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        w = a[1][0] * b[0][1] + a[1][1] * b[1][1]
        return [[x, y], [z, w]]

    # Helper function for matrix exponentiation
    def power(matrix, n):
        result = [[1, 0], [0, 1]]  # Identity matrix

        while n > 0:
            if n % 2 == 1:
                result = multiply(result, matrix)
            matrix = multiply(matrix, matrix)
            n //= 2

        return result

    # Calculate the kth Fibonacci number
    matrix = [[1, 1], [1, 0]]
    result = power(matrix, k - 1)
    return result[0][0]