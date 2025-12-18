"""
QUESTION:
Write a function called `get_prime_numbers` that returns a list of all prime numbers in a given range. The function should take two parameters, `start` and `end`, and return a list of prime numbers within the range from `start` to `end` (inclusive). The function should work efficiently for large ranges.
"""

def get_prime_numbers(start, end):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [n for n in range(start, end + 1) if is_prime(n)]