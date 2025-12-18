"""
QUESTION:
Write a function `filter_primes` that takes a list of integers as input and returns a new list containing only the prime numbers. 

The function should implement its own algorithm to determine the primality of each number and should not use any built-in functions or libraries for this purpose. 

Negative integers in the input list should be treated the same as their positive counterparts when determining their primality. The input list will only contain integers and will have a length of less than or equal to 1000.
"""

def filter_primes(lst):
    """
    This function filters out the prime numbers from a given list of integers.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A new list containing only the prime numbers.
    """
    def is_prime(n):
        """
        This helper function checks if a number is prime.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [n for n in lst if is_prime(abs(n))]