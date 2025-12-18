"""
QUESTION:
Write a function `prime_sum(n)` that calculates the sum of all prime numbers from 0 to `n` and the sum of all even composite numbers from 0 to `n`. The function should take an integer `n` as input, where `n` is a non-negative integer.
"""

def prime_sum(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_even_composite(num):
        if num < 4 or num % 2 != 0:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return True
        return False

    prime_sum = 0
    even_composite_sum = 0
    for num in range(n + 1):
        if is_prime(num):
            prime_sum += num
        elif is_even_composite(num):
            even_composite_sum += num
    return (prime_sum, even_composite_sum)