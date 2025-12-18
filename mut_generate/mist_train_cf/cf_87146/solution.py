"""
QUESTION:
Write a function `product_of_four_primes` to calculate the product of four unique prime numbers less than 100. The function should return the product of the first four unique prime numbers it encounters.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def product_of_four_primes():
    primes = []
    num = 2
    while len(primes) < 4:
        if is_prime(num):
            primes.append(num)
        num += 1
    product = 1
    for prime in primes:
        product *= prime
    return product