"""
QUESTION:
Create a function named `prime_range(start, end)` that generates a list of prime numbers within the given range from `start` to `end` (inclusive), where `start` and `end` are integers and `start` is less than or equal to `end`. The function should return a list of integers.
"""

def prime_range(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        max_div = int(n**0.5) + 1
        for div in range(3, max_div, 2):
            if n % div == 0:
                return False
        return True

    return [n for n in range(start, end+1) if is_prime(n)]