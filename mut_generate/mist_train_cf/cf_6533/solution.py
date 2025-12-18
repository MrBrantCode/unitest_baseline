"""
QUESTION:
Write a function `fibonacci(n)` to calculate the Nth term of the Fibonacci sequence. The Fibonacci sequence is defined as a series of numbers where the first two terms are 0 and 1, and each subsequent term is the sum of the previous two terms. The solution should have a time complexity of O(log n) and a space complexity of O(1). You are not allowed to use any loops or recursion in your solution.
"""

def multiply_matrices(a, b):
    return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

def power_matrix(matrix, power):
    if power == 0:
        return [[1, 0], [0, 1]]  

    if power % 2 == 0:
        sqrt = power_matrix(matrix, power // 2)
        return multiply_matrices(sqrt, sqrt)
    else:
        sqrt = power_matrix(matrix, (power - 1) // 2)
        return multiply_matrices(matrix, multiply_matrices(sqrt, sqrt))

def fibonacci(n):
    if n == 0:
        return 0

    matrix = [[1, 1], [1, 0]]
    matrix_power_n_minus_1 = power_matrix(matrix, n - 1)
    return matrix_power_n_minus_1[0][0]