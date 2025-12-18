"""
QUESTION:
Write a function `product_of_primes(N)` that calculates the product of the first N prime numbers, where N is a given positive integer. The function should return the product as an integer. The input N is a positive integer, and the function should handle this input correctly.
"""

def product_of_primes(N):
    primes = []
    num = 2
    while len(primes) < N:
        if is_prime(num):
            primes.append(num)
        num += 1
    product = 1
    for prime in primes:
        product *= prime
    return product

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True