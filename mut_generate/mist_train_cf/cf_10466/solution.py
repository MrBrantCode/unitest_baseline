"""
QUESTION:
Create a function `print_primes(n)` that prints all prime numbers less than or equal to the given integer `n`. The function should be able to handle any positive integer `n`. The function should return a list of prime numbers.
"""

def print_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [num for num in range(2, n + 1) if is_prime(num)]
    return primes