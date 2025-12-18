"""
QUESTION:
Write a function named `find_primes` that takes an integer `n` as input and returns a list of all prime numbers from 2 to `n`. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def find_primes(n):
    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes