"""
QUESTION:
Create a function `list_primes` that takes two integer parameters, `start` and `end`, and returns a list of all prime numbers between `start` and `end` (inclusive). The function should be able to handle any integer range, including negative numbers and zero.
"""

def list_primes(start, end):
    def is_prime(num):
        if num < 2:
            return False
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

    return [num for num in range(start, end + 1) if is_prime(num)]