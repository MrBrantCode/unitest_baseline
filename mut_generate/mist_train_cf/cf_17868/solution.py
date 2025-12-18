"""
QUESTION:
Write a function named `fibonacci(k)` to find the kth element in the Fibonacci sequence. The function should have a time complexity of O(log n) and not use recursion. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The input `k` is the position of the Fibonacci number to be found.
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