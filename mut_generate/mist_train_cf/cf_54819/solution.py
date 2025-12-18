"""
QUESTION:
Implement the `get_prime` function to generate all prime numbers up to a given number `n`. The function should return a list of prime numbers. Use the Sieve of Eratosthenes algorithm for this task.
"""

def get_prime(n):
    sieve = [True] * (n+1)
    p = 2
    while (p * p <= n):
        if (sieve[p] == True):
            for i in range(p * p, n+1, p):
                sieve[i] = False
        p += 1
 
    prime = []
    for p in range(2, n+1):
        if sieve[p]:
            prime.append(p)
    return prime