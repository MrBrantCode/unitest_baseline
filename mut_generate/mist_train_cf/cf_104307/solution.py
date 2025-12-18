"""
QUESTION:
Create a function `sum_of_primes_in_range` that takes two parameters, `start` and `end`, representing the range of numbers. The function should calculate and return the sum of all prime numbers within this range, including the `start` and `end` values if they are prime. The range is inclusive.
"""

def sum_of_primes_in_range(start, end):
    """
    Calculate the sum of all prime numbers within the given range, 
    including the start and end values if they are prime.

    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        int: The sum of all prime numbers in the range.
    """

    def is_prime(num):
        """Check if a number is prime."""
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = sum(num for num in range(start, end + 1) if is_prime(num))
    return prime_sum