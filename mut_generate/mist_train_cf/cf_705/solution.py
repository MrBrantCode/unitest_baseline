"""
QUESTION:
Create a function named `sieve_of_eratosthenes` that takes an integer `n` as input and returns a list of all prime numbers smaller than or equal to `n`, along with the sum of these prime numbers. The function should use the Sieve of Eratosthenes algorithm. The function should not take any other parameters and should only return a tuple containing a list of prime numbers and their sum.
"""

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    
    primes = []
    prime_sum = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            prime_sum += i
    
    return primes, prime_sum