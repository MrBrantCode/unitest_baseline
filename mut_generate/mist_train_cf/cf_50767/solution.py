"""
QUESTION:
Create a function named `is_prime(n,m)` that returns a dictionary containing the primality truth value for all integers between `n` and `m` inclusive. The function must use the Sieve of Eratosthenes approach for testing primality. Note that the function is expected to work correctly only if `n` is no less than 2, as 1 is not considered a prime number.
"""

def entrance(n, m):
    sieve = {i: True for i in range(2, m + 1)}
    
    for i in range(2, int(m ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, m + 1, i):
                sieve[j] = False
                
    return {i: sieve[i] for i in range(n, m + 1) if i in sieve}