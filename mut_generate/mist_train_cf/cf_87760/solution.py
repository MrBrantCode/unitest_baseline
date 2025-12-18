"""
QUESTION:
Write a function `fibonacci(k)` to find the kth element in the Fibonacci sequence with a time complexity of O(log n) and without using recursion. The function should be space efficient and should not use any extra data structures apart from a constant amount of variables.
"""

def fibonacci(k):
    if k < 0:
        return None
    elif k <= 1:
        return k

    matrix = [[1, 1], [1, 0]]
    result = [[1, 0], [0, 1]]

    while k > 0:
        if k % 2 == 1:
            result = multiply(result, matrix)
        matrix = multiply(matrix, matrix)
        k //= 2

    return result[0][1]

def multiply(matrix1, matrix2):
    a = matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0]
    b = matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]
    c = matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]
    d = matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]
    return [[a, b], [c, d]]