"""
QUESTION:
Create a function named `primes_sieve` that takes an integer `n` and returns a list of all prime numbers less than or equal to `n` using the Sieve of Eratosthenes algorithm. The function should have a time complexity of O(n log log n) and a space complexity of O(n).
"""

def primes_sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes