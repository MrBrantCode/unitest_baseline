"""
QUESTION:
Create a function `generate_prime_numbers` that takes an integer `n` as input and returns a list of the first `n` prime numbers in descending order. The function should have a time complexity of O(n log(log(n))) and should not use any built-in prime number generation functions or libraries.
"""

def generate_prime_numbers(n):
    primes = []  
    sieve = [True] * (n+1)  
    
    p = 2
    
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n+1, p):
                sieve[i] = False
        p += 1
    
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
    
    return primes[::-1] 