"""
QUESTION:
Create a function named `find_twin_cousin_primes(n)` that finds all twin prime numbers and cousin prime numbers between 2 and a given integer `n`. Twin prime numbers are prime numbers that differ by 2, and cousin prime numbers are prime numbers that differ by 4. The function should return two lists, one for twin primes and one for cousin primes, where each prime number pair is represented as a tuple.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_cousin_primes(n):
    twin_primes = []
    cousin_primes = []
    for i in range(2, n):
        if is_prime(i) and is_prime(i + 2):
            twin_primes.append((i, i + 2))
        if is_prime(i) and is_prime(i + 4):
            cousin_primes.append((i, i + 4))
    return twin_primes, cousin_primes