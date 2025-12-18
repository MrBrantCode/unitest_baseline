"""
QUESTION:
Write a function `sum_of_primes(n)` that takes an integer `n` as input and returns the sum of all prime numbers less than or equal to `n`. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def sum_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(2, n + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum