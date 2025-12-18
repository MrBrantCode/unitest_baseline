"""
QUESTION:
Write a function `SieveOfEratosthenes(n)` that finds all prime numbers in a given range from 1 to `n` using the Sieve of Eratosthenes algorithm. The function should return a list of prime numbers.
"""

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    
    prime_nums_list = []
    for p in range(2, n):
        if prime[p]:
            prime_nums_list.append(p)
    
    return prime_nums_list