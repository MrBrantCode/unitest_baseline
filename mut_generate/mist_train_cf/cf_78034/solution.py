"""
QUESTION:
Write a function `solve_problem(matrix)` that takes a 2D list of integers as input, and returns a tuple containing the sum of all prime numbers in the matrix, a list of sums of each row in the matrix, and a list of sums of each column in the matrix. The input matrix is not empty and does not contain empty lists.
"""

import numpy as np

def solve_problem(matrix):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5)+1):
            if (number % i) == 0:
                return False
        return True

    sum_of_primes = sum(number for lst in matrix for number in lst if is_prime(number))
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(col) for col in zip(*matrix)]
    return sum_of_primes, row_sums, col_sums