"""
QUESTION:
Create a function `has_prime` that takes a list of integers as input and returns True if at least one number in the list is a prime number. The function should return a boolean value.
"""

def has_prime(numbers):
    """
    Checks if at least one number in the list is a prime number.

    Args:
    numbers (list): A list of integers.

    Returns:
    bool: True if at least one number in the list is prime, False otherwise.
    """

    def is_prime(n):
        """Checks if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in numbers:
        if is_prime(num):
            return True
    return False