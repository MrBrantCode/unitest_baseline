"""
QUESTION:
Implement a function `sum_of_primes(start, end)` that calculates the sum of all prime numbers within the inclusive range from `start` to `end`. The function should take two integers, `start` and `end`, as input and return the sum of prime numbers. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    prime_sum = 0
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum