"""
QUESTION:
Create a function `find_prime_numbers` that takes a positive integer `n` greater than 1 as input and returns a list of all prime numbers less than `n`. The function should use the Sieve of Eratosthenes algorithm and return the prime numbers in ascending order. The input `n` will be a positive integer greater than 1.
"""

def find_prime_numbers(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False  

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n+1, p):
                is_prime[i] = False
        p += 1

    primes = [i for i in range(2, n) if is_prime[i]]
    return primes