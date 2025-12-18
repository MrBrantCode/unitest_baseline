"""
QUESTION:
Write a function named `generate_primes` that generates all prime numbers from 1 to 'n'. The function should return a list of prime numbers. The function should not include 1 as a prime number. The input 'n' is a positive integer.
"""

def generate_primes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p] == True:
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    # Collect and return all prime numbers
    primes = []
    for p in range(2, n):
        if prime[p]:
            primes.append(p)
    return primes