"""
QUESTION:
Create a function named `check_three_prime_product` that takes one argument `num` (less than 100). This function should return `True` if `num` is a product of exactly three prime numbers, and `False` otherwise.
"""

def check_three_prime_product(num):
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

    primes = []
    for i in range(2, num):
        if num % i == 0 and is_prime(i):
            primes.append(i)
        if len(primes) > 3:
            break

    if len(primes) != 3:
        return False

    product = 1
    for prime in primes:
        product *= prime

    return product == num