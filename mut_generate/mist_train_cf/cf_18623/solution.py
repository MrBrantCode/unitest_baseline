"""
QUESTION:
Write a function `prime_sum(n)` that calculates the sum of all prime numbers from 0 to `n` and the sum of all composite numbers from 0 to `n`. The function should return both sums. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself, and a composite number is a positive integer that has at least one positive divisor other than 1 and itself.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_sum(n):
    prime_sum = 0
    composite_sum = 0
    for num in range(n + 1):
        if is_prime(num):
            prime_sum += num
        else:
            composite_sum += num
    return prime_sum, composite_sum