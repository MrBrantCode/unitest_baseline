"""
QUESTION:
Write a function `generate_primes` to generate a list of prime numbers within a given range (inclusive), implemented using recursive function calls and memoization. The function should only use odd numbers to check for primality and must not utilize any built-in library functions to check for prime numbers. The function should take three parameters: the start of the range, the end of the range, and a list to store the prime numbers found.
"""

def is_prime(n, primes):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for prime in primes:
        if prime * prime > n:
            return True
        if n % prime == 0:
            return False

    return True

def generate_primes(start, end, primes):
    if start > end:
        return []

    if is_prime(start, primes):
        primes.append(start)
        return [start] + generate_primes(start + 2, end, primes)

    return generate_primes(start + 2, end, primes)