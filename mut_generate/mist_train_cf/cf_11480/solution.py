"""
QUESTION:
Write a function named `find_primes` that finds all prime numbers within a given range. The function should take two parameters: `min_num` and `max_num`, which represent the range's lower and upper bounds (inclusive). It should return a list of prime numbers within this range.
"""

def find_primes(min_num, max_num):
    """
    Finds all prime numbers within a given range.

    Args:
        min_num (int): The lower bound of the range (inclusive).
        max_num (int): The upper bound of the range (inclusive).

    Returns:
        list: A list of prime numbers within the given range.
    """
    def is_prime(num):
        """Checks if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in range(min_num, max_num + 1) if is_prime(num)]