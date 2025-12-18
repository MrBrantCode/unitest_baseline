"""
QUESTION:
Create a recursive function `sum_of_n_primes(n)` that calculates the sum of the first n prime numbers, where n is a positive integer. The function should not use any loops or iteration other than the implicit recursion, but may use helper functions.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_n_primes(n):
    def helper(count, sum_primes, current):
        if count == 0:
            return sum_primes
        if is_prime(current):
            return helper(count - 1, sum_primes + current, current + 1)
        return helper(count, sum_primes, current + 1)

    return helper(n, 0, 2)