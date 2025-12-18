"""
QUESTION:
Create a function called `find_twin_primes` that takes two parameters, `start` and `end`, representing a range of numbers. This function should identify all pairs of twin primes within the given range, where twin primes are prime numbers that are either 2 less or 2 more than another prime number, and return these pairs. The function should be able to handle edge cases.
"""

def find_twin_primes(start, end):
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

    twin_primes = []
    for i in range(start, end):
        j = i + 2
        # check if both numbers are prime
        if is_prime(i) and is_prime(j):
            twin_primes.append([i, j])

    return twin_primes