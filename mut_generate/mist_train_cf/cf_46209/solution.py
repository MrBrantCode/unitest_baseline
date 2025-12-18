"""
QUESTION:
Implement a function called `sieve_of_eratosthenes` that returns all prime numbers up to a given integer `n`. The function should use the Sieve of Eratosthenes algorithm and return a list of prime numbers. The input `n` is an integer greater than 1.
"""

def sieve_of_eratosthenes(n):
    numbers = [True] * (n+1)
    p = 2
    while p ** 2 <= n:
        if numbers[p] == True:
            for i in range(p **2, n+1, p):
                numbers[i] = False
        p += 1
        
    primes = []
    for i in range(2, len(numbers)):
        if numbers[i]:
            primes.append(i)
    return primes