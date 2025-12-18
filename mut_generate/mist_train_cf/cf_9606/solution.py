"""
QUESTION:
Write a function called `find_primes(n)` that returns a list of all prime numbers up to `n` using the Sieve of Eratosthenes algorithm. The function should not use any built-in functions or libraries for this purpose. The input `n` is a positive integer, and the output should be a list of integers.
"""

def entrance(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
    
    return primes