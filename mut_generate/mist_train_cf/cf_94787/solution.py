"""
QUESTION:
Write a function `sum_of_prime_squares_and_count` that calculates the sum of the squares of all prime numbers and the count of prime numbers between 1 and a given number `n` (inclusively). The function should return a tuple containing the sum of the squares and the count. Assume `n` is a positive integer.
"""

import math

def sum_of_prime_squares_and_count(n):
    def is_prime(i):
        if i < 2:
            return False
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                return False
        return True

    sum_of_squares = 0
    count = 0

    for i in range(1, n + 1):
        if is_prime(i):
            sum_of_squares += i ** 2
            count += 1

    return sum_of_squares, count