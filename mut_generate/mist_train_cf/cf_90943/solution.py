"""
QUESTION:
Create a function `find_twin_primes(n)` to find all twin prime numbers between 2 and a given integer `n`. A twin prime number is a prime number that differs by 2. The function should return a list of tuples, where each tuple contains a pair of twin prime numbers.
"""

def find_twin_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    twin_primes = []
    for i in range(2, n):
        if is_prime(i) and is_prime(i + 2):
            twin_primes.append((i, i + 2))
    return twin_primes