"""
QUESTION:
Write a Python function `find_primes(num)` that returns the first 'num' prime numbers, where 'num' is a positive integer. The function should start checking from the number 2.
"""

def find_primes(num):
    primes = []
    i = 2
    while len(primes) < num:
        if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
            primes.append(i)
        i += 1
    return primes