"""
QUESTION:
Create a function `prime_numbers_less_than(n)` that returns a list of all prime numbers less than the given integer `n`. The function should handle integers greater than or equal to 2.
"""

def prime_numbers_less_than(n):
    """
    Returns a list of all prime numbers less than the given integer n.

    Args:
        n (int): The upper limit for finding prime numbers.

    Returns:
        list: A list of prime numbers less than n.
    """
    def is_prime(num):
        """Helper function to check if a number is prime."""
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    
    return [i for i in range(2, n) if is_prime(i)]