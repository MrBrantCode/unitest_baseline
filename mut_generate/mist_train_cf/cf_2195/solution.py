"""
QUESTION:
Create a recursive function `sum_prime_numbers(start, end)` that calculates the sum of all prime numbers between `start` and `end` (inclusive), excluding numbers that are divisible by both 3 and 7. The function should not use any loops or external libraries for prime number generation.
"""

def sum_prime_numbers(start, end):
    def is_prime(n, i=2):
        # Base cases
        if n <= 2:
            return n == 2
        if n % i == 0:
            return False
        if i * i > n:
            return True

        return is_prime(n, i + 1)

    if start > end:
        return 0

    if start % 21 == 0:  # Exclude numbers divisible by both 3 and 7
        return sum_prime_numbers(start + 1, end)

    if is_prime(start):
        return start + sum_prime_numbers(start + 1, end)
    else:
        return sum_prime_numbers(start + 1, end)