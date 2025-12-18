"""
QUESTION:
Write a function `get_nth_primes(n)` that returns the nth and (n+1)th prime numbers in ascending order. The function should use the helper function `is_prime(num)` to check if a number is prime. The function should return the prime numbers without duplicates and in ascending order.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_nth_primes(n):
    primes = []
    num = 2
    while len(primes) < n + 1:
        if is_prime(num):
            primes.append(num)
        num += 1
    return sorted(primes)[-2:] 