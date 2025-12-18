"""
QUESTION:
Write a function `sum_of_primes` that calculates the sum of all prime numbers between a given range, excluding any prime numbers that contain the digit 5. The function should take two integers as input: `lower_limit` and `upper_limit`, representing the range limits.
"""

def sum_of_primes(lower_limit, upper_limit):
    def is_prime(n):
        if n < 2 or '5' in str(n):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(num for num in range(lower_limit, upper_limit + 1) if is_prime(num))