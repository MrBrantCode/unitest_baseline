"""
QUESTION:
Write a function `sum_of_prime_in_matrix(matrix)` to find the sum of all prime numbers in a given three-dimensional matrix of integers. The function should be optimized for large inputs by implementing an efficient algorithm to determine whether a number is prime.
"""

import math

def sum_of_prime_in_matrix(matrix):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = math.sqrt(n) + 1
        for i in range(3, int(sqrt_n), 2):
            if n % i == 0:
                return False
        return True

    total_sum = 0
    for layer in matrix:
        for row in layer:
            for num in row:
                if is_prime(num):
                    total_sum += num
    return total_sum