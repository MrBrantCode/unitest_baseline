"""
QUESTION:
Write a function `is_mersenne_prime` that checks if a given prime number `p` is a Mersenne prime, which is a prime number of the form 2^n - 1 for some integer `n`. The function should return `True` if `p` is a Mersenne prime and `False` otherwise. Also, write a function `generate_primes` that generates a list of prime numbers up to a given number `n`. Then, use these functions to return a list of all Mersenne primes within the generated prime numbers list.
"""

def generate_primes(n):
    sieve = [True] * (n+1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]: 
            sieve[x*2:n+1:x] = [False] * len(sieve[x*2:n+1:x])
    return [x for x in range(2, n) if sieve[x]]

def is_mersenne_prime(p):
    """Check if a prime number p is a Mersenne prime."""
    n = 2
    while (2 ** n - 1) <= p:
        if (2 ** n - 1) == p:
            return True
        n += 1
    return False