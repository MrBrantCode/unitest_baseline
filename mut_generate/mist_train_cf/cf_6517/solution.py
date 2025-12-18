"""
QUESTION:
Create a function named `nth_prime` that takes an integer `n` as input, where 1 ≤ n ≤ 10^5, and returns the nth prime number. The function should efficiently calculate prime numbers without using pre-calculated lists or libraries.
"""

def nth_prime(n):
    primes = []  # List to store prime numbers
    i = 2  # Start checking for primes from 2
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if prime * prime > i:
                break
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 1
    return primes[-1]