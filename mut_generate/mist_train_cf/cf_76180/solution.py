"""
QUESTION:
Implement a function `generate_primes(lower, upper)` that generates a list of prime numbers between two numbers `lower` and `upper` (both inclusive) using the Sieve of Eratosthenes algorithm. The function should be efficient enough to work with large inputs of `lower` and `upper`.
"""

def generate_primes(lower, upper):
    """
    Generates a list of prime numbers between two numbers 'lower' and 'upper' (both inclusive) using the Sieve of Eratosthenes algorithm.

    Args:
        lower (int): The lower bound of the range (inclusive).
        upper (int): The upper bound of the range (inclusive).

    Returns:
        list: A list of prime numbers between 'lower' and 'upper'.
    """
    sieve = [True] * (upper + 1)
    p = 2
    while p*p <= upper:
        if sieve[p] == True:
            for i in range(p*p, upper+1, p):
                sieve[i] = False
        p += 1
    
    primes = []
    for p in range(max(2, lower), upper+1):
        if sieve[p]:
            primes.append(p)
    return primes