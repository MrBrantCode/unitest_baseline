"""
QUESTION:
Implement the `sieve_of_eratosthenes` function to find all prime numbers up to a given number `n` using the Sieve of Eratosthenes algorithm. The function should return a list of prime numbers. 

The implementation must have a time complexity of O(n log log n) and should not use any built-in function or library to solve the problem.
"""

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i**2, n + 1, i):
                is_prime[j] = False
    
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    
    return primes