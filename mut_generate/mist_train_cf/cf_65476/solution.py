"""
QUESTION:
Write a function `sum_of_primes_in_matrix(matrix)` that calculates the sum of all prime numbers in a given matrix of integers. The function should take a 2D list of integers as input and return the sum of prime numbers found in the matrix.
"""

import math

def sum_of_primes_in_matrix(matrix):
    prime_sum = 0
    for row in matrix:
        for num in row:
            if num > 1 and (num == 2 or (num % 2 != 0 and all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2)))):
                prime_sum += num
    return prime_sum