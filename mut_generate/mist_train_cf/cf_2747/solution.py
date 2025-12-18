"""
QUESTION:
Write a function to find the sum of all prime numbers from 1 to n that are not multiples of 3 or 5.
"""

def sum_of_primes(n):
    """
    This function calculates the sum of all prime numbers from 1 to n that are not multiples of 3 or 5.

    Args:
        n (int): The upper limit for the range of numbers to check.

    Returns:
        int: The sum of all prime numbers from 1 to n that are not multiples of 3 or 5.
    """
    def is_prime(num):
        """
        Helper function to check if a number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum(num for num in range(1, n+1) if num % 3 != 0 and num % 5 != 0 and is_prime(num))