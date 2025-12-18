"""
QUESTION:
Write a function `sum_of_squares_and_prime_count` that calculates the sum of the squares of all prime numbers between 1 and a given upper limit (inclusively) and returns this sum along with the count of prime numbers found in the given range. The function should take one integer argument `upper_limit`.
"""

import math

def sum_of_squares_and_prime_count(upper_limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    sum_of_squares = 0
    count = 0
    for i in range(1, upper_limit + 1):
        if is_prime(i):
            sum_of_squares += i ** 2
            count += 1
    return sum_of_squares, count