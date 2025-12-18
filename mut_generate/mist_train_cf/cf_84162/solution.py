"""
QUESTION:
Create a function named `solve(n)` that calculates the quantity of unique prime numbers and their sum below a given number `n`. The given number `n` is within the range 100 <= n <= 10^6. The function should return a tuple containing two values: the count of unique prime numbers and the sum of these prime numbers.
"""

def solve(n):
    primes = [True] * (n+1)
    p = 2
    while p**2 <= n:
        if primes[p] == True:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1

    prime_numbers = [p for p in range(2, n) if primes[p]]
    return len(prime_numbers), sum(prime_numbers)