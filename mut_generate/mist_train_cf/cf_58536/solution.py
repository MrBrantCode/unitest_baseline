"""
QUESTION:
Write a function `multiply_primes(limit)` that calculates the product of all prime numbers less than the given limit. The function should return the product of these prime numbers. The input limit is a positive integer, and the function should handle limits greater than 1.
"""

def multiply_primes(limit):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    result = 1
    for i in range(2, limit):
        if is_prime(i):
            result *= i
    return result