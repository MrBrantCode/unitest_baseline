"""
QUESTION:
Write a function `sum_and_locations_of_primes` that takes a matrix of integers as input. The function should return the sum of all prime numbers in the matrix and the positions (row, column) of each prime number. The function should have a time complexity of O(n*m*sqrt(x)), where 'n' and 'm' are the dimensions of the matrix, and 'x' is an element of the matrix. The prime detection algorithm used should be optimized, such as a simplified version of the Sieve of Eratosthenes, that eliminates unnecessary checks by ignoring even numbers and only checking divisibility up to the square root of the number.
"""

import math

def sum_and_locations_of_primes(matrix):
    sum_of_primes = 0
    locations_of_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, math.isqrt(n) + 1, 2):
            if n % i == 0:
                return False
        return True

    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if is_prime(num):
                sum_of_primes += num
                locations_of_primes.append((i, j))

    return sum_of_primes, locations_of_primes