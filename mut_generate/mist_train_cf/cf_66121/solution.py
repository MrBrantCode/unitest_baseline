"""
QUESTION:
Create a function `find_primes` that computes all prime numbers less than or equal to a given integer `n`. The function should take `n` as an argument and return a list of prime numbers. The function should only include prime numbers starting from 2.
"""

def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    return primes