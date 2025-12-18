"""
QUESTION:
Write a function named SieveOfEratosthenes that generates a series of prime numbers up to a given number (n) using the Sieve of Eratosthenes algorithm. The function should take an integer (n) as input and return a list of prime numbers. Optimize the algorithm for time and space complexity.
"""

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n) if prime[p]]