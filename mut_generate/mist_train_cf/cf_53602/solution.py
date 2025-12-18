"""
QUESTION:
Write a function `is_product_of_three_primes(n)` that returns `True` if the input number `n` is the product of exactly three prime numbers and `False` otherwise, given that `n` is less than 100.
"""

def is_product_of_three_primes(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    prime_factors = 0

    for prime in primes:
        while n % prime == 0:
            n = n // prime
            prime_factors += 1
            
    return prime_factors == 3 and n == 1