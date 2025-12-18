"""
QUESTION:
Write a function `sieveOfEratosthenes(n)` that generates the first n prime numbers using the Sieve of Eratosthenes method. The function should return a list of the first n prime numbers. Note that the input number n may not directly correspond to the upper limit of the sieve, but rather the desired count of prime numbers to be returned.
"""

def entrance(n):
    limit = 1000
    while True:
        primes = [True for i in range(limit+1)]
        p = 2
        while(p * p <= limit):
            if (primes[p] == True):
                for i in range(p * p, limit+1, p):
                    primes[i] = False
            p += 1

        prime_numbers = []
        for p in range(2, limit+1):
            if primes[p]:
                prime_numbers.append(p)
        if len(prime_numbers) >= n:
            return prime_numbers[:n]
        limit *= 2