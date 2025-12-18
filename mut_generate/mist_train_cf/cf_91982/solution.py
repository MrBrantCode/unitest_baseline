"""
QUESTION:
Create a function `sum_prime_numbers(m, n)` that takes two positive integers `m` and `n` as input where `m < n`. The function should return the sum of all prime numbers in the range from `m` to `n` inclusive.
"""

def sum_prime_numbers(m, n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(m, n + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum