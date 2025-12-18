"""
QUESTION:
Write a function `sieve_of_eratosthenes` that generates a list of prime numbers up to a given limit `n` and use this function to find the sum of the first 100 prime numbers between 10000 and 20000. The function should take an integer `n` as input and return a list of prime numbers.
"""

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False  

    p = 2
    while p**2 <= n:
        if is_prime[p]:
            for i in range(p**2, n+1, p):
                is_prime[i] = False
        p += 1

    primes = []
    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)

    return primes