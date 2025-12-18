"""
QUESTION:
Write a function `find_primes(n)` to return a list of all prime numbers less than or equal to `n`. The input `n` is a positive integer.
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