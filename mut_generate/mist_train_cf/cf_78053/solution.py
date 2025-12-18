"""
QUESTION:
Create a function named `prime_numbers` that takes an integer `n` as input, where `n` can be up to 10^5. The function should return a list of all prime numbers between 2 and `n` (inclusive), or an error message if `n` is not a positive integer. The function should be optimized to minimize the number of iterations performed to identify a prime.
"""

def prime_numbers(n):
    # Check the input
    if not isinstance(n, int) or n <= 0:
        return 'Error: The input must be a positive integer'

    # Use sieve of Eratosthenes for efficient prime checking
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while (p * p <= n): 
        if (primes[p] == True): 
            for i in range(p * p, n+1, p): 
                primes[i] = False
        p += 1
    return [p for p in range(2, n+1) if primes[p]]