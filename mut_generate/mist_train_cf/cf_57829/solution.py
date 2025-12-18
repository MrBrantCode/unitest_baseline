"""
QUESTION:
Create a function `sieve_of_eratosthenes(n)` that generates a list of all prime numbers between 500 and `n` (inclusive) using the Sieve of Eratosthenes algorithm. The function should return a list of prime numbers within the specified range. The input `n` is an integer greater than 500.
"""

def sieve_of_eratosthenes(n):
    sieve = [True] * (n+1)
    p = 2
    while(p**2 <= n):
        if(sieve[p] is True):
            for i in range(p**2, n+1, p):
                sieve[i] = False
        p += 1

    primes = []
    for i in range(500, n+1):  # Include n in the range
        if sieve[i]:
            primes.append(i)

    return primes