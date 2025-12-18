"""
QUESTION:
Write a function `SieveOfEratosthenes` that calculates the sum of all prime numbers within a given range [n, limit]. The function should take two parameters, `n` and `limit`, where `n` is the upper limit of the range and `limit` is the lower limit of the range. Implement the function using the Sieve of Eratosthenes algorithm to efficiently handle large input numbers.
"""

def SieveOfEratosthenes(n, limit):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    sum = 0
    for p in range(limit, n):
        if prime[p]:
            sum += p
    return sum