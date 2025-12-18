"""
QUESTION:
Implement a function `sum_of_primes(start, end)` that calculates the sum of all prime numbers within the inclusive range from `start` to `end`. The function should take two integers, `start` and `end`, as input and return the sum of all prime numbers within this range. The function must be able to handle cases where `start` is less than 2, in which case it should start checking for prime numbers from 2.
"""

def sum_of_primes(start: int, end: int) -> int:
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum