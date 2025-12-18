"""
QUESTION:
Write a function named `sum_fib_in_matrix` that calculates the sum of all Fibonacci numbers present in a given matrix. The function should take a 2D list of integers (matrix) as input and return the sum of all Fibonacci numbers in the matrix. There is no restriction on the size of the matrix or the range of values it can contain.
"""

def sum_fib_in_matrix(matrix):
    """Function to sum all fibonacci numbers in a matrix"""
    def is_perfect_square(x):
        s = int(x ** 0.5)
        return s * s == x

    def is_fibonacci(n):
        return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

    total = 0
    for row in matrix:
        for element in row:
            if is_fibonacci(element):
                total += element
    return total