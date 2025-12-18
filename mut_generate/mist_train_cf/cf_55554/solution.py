"""
QUESTION:
Write a function `get_primes(n)` that generates a list of the first `n` distinct prime numbers between 10 and 100 in descending order.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    num = 100 # start from 100
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num -= 1
    return primes