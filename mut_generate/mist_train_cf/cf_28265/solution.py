"""
QUESTION:
Write a function `sum_of_primes` that takes two integers `start` and `end` and returns the sum of all prime numbers within the inclusive range `[start, end]`. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. If no prime numbers exist within the given range, return 0.
"""

def sum_of_primes(start: int, end: int) -> int:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum