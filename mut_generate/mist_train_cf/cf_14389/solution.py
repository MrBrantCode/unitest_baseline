"""
QUESTION:
Write a function called `sum_of_primes` that takes two integers `lower` and `upper` as input and returns the sum of all prime numbers between `lower` and `upper` (inclusive). The function should not take any other parameters, and the input range is guaranteed to be within the valid range for integer values in Python.
"""

def sum_of_primes(lower, upper):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_list = [num for num in range(lower, upper + 1) if is_prime(num)]
    return sum(prime_list)