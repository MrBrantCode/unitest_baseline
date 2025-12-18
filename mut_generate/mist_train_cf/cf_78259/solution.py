"""
QUESTION:
Create a function `print_primes(n)` that takes an integer `n` and returns the first `n` prime numbers. A prime number is a number that has only two distinct natural number divisors: 1 and the number itself. Use a 'while' loop control structure in your implementation and optimize the algorithm for efficiency.
"""

def print_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if all(candidate % prime != 0 for prime in primes):
            primes.append(candidate)
        candidate += 1
    return primes