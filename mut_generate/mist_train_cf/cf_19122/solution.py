"""
QUESTION:
Create a function `prime_multiplication_table(num)` that prints a multiplication table of a given number `num`, but only for prime numbers less than or equal to `num`. The function should use a helper function `is_prime(num)` that checks whether a given number `num` is prime or not. The `is_prime(num)` function should return `True` if `num` is prime, and `False` otherwise.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_multiplication_table(num):
    primes = [x for x in range(2, num+1) if is_prime(x)]
    for i in range(1, num+1):
        for prime in primes:
            print(i * prime, end='\t')
        print()