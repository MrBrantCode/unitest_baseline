"""
QUESTION:
Write a function called `prime_at_multiple_of_3` that takes an array of integers and returns a new array containing only the prime numbers from the original array, but only if their index in the original array is a multiple of 3.
"""

def prime_at_multiple_of_3(arr):
    """
    Returns a new array containing only the prime numbers from the original array, 
    but only if their index in the original array is a multiple of 3.

    Args:
        arr (list): The input array of integers.

    Returns:
        list: A new array containing the prime numbers at indices that are multiples of 3.
    """
    def is_prime(n):
        """
        Helper function to check if a number is prime.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [x for i, x in enumerate(arr) if i % 3 == 0 and is_prime(x)]