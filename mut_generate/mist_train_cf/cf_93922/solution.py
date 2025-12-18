"""
QUESTION:
Write a function named `sieve_of_eratosthenes` that takes two integers `start` and `end` as input and returns a list of prime numbers between `start` and `end` (inclusive) using the Sieve of Eratosthenes algorithm. The function should be efficient for large ranges of numbers.
"""

def sieve_of_eratosthenes(start, end):
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while p * p <= end:
        if is_prime[p] == True:
            for i in range(p * p, end + 1, p):
                is_prime[i] = False
        p += 1
    
    primes = []
    for i in range(start, end + 1):
        if is_prime[i]:
            primes.append(i)
    
    return primes