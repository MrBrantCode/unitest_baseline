"""
QUESTION:
Design a function called `sum_of_primes` that takes a list of integers as input and returns the sum of all prime numbers in the list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(numbers):
    prime_sum = 0
    for num in numbers:
        if is_prime(num):
            prime_sum += num
    return prime_sum