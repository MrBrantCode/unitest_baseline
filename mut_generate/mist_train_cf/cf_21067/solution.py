"""
QUESTION:
Write a function named `contains_only_primes` that takes a string of digits as input and returns `True` if all the digits are prime numbers and `False` otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def contains_only_primes(string):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for char in string:
        if not is_prime(int(char)):
            return False
    return True