"""
QUESTION:
Write a function called `get_prime_numbers(n)` that takes in an integer `n` as a parameter and returns a list of the first `n` prime numbers. Implement the function using the Sieve of Eratosthenes algorithm. The function should not hardcode any prime numbers or the range of numbers to be checked, and it should be efficient enough to handle larger values of `n`.
"""

import math

def get_prime_numbers(n):
    limit = 1000  # initialize limit
    while True:
        is_prime = [True] * (limit+1)  
        is_prime[0] = False
        is_prime[1] = False
        
        for p in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[p]:
                for i in range(p*p, limit+1, p):
                    is_prime[i] = False
        
        prime_numbers = []
        for i in range(2, limit+1):
            if is_prime[i]:
                prime_numbers.append(i)
                if len(prime_numbers) == n:
                    return prime_numbers
        limit *= 2  # increase limit and try again