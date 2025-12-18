"""
QUESTION:
Create a function `prime_numbers_in_range` that generates a list of prime numbers within a specified range. The function should return a list of prime numbers between 1 and the given number (inclusive). The input should be an integer and the output should be a list of integers.
"""

def prime_numbers_in_range(n):
    """Generates a list of prime numbers within a specified range."""
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in range(2, n + 1) if is_prime(num)]