"""
QUESTION:
Write a function named `sum_of_primes` to calculate the sum of all prime numbers within a given range. The function should take two parameters, `lower` and `upper`, representing the lower and upper bounds of the range (inclusive), and return the sum of prime numbers within this range. The range is guaranteed to be non-empty and the lower bound is less than or equal to the upper bound.
"""

def sum_of_primes(lower, upper):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(num for num in range(lower, upper + 1) if is_prime(num))