"""
QUESTION:
Create a generator function named `primes` that yields an infinite sequence of prime numbers, starting from 2, where each number is generated on-the-fly. The function should use an internal helper function `is_prime` to check if a given number is prime or not. The helper function should return `False` for numbers less than 2 and check divisibility up to the square root of the number. The `primes` function should yield the next prime number when its `next` method is called.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def entrance():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1