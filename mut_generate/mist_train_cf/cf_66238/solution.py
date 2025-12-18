"""
QUESTION:
Construct a function named `get_prime_numbers` that takes two parameters, `start` and `end`, representing the start and end points of a range (inclusive), and returns a list of all prime numbers within this range.
"""

def get_prime_numbers(start, end):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in range(start, end + 1) if is_prime(num)]