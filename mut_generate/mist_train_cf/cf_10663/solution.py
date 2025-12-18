"""
QUESTION:
Write a function `find_divisible_primes` that takes a list of integers as input and returns a list of numbers that are divisible by both 3 and 5, and are also prime numbers.
"""

def find_divisible_primes(numbers):
    """
    Returns a list of numbers from the input list that are divisible by both 3 and 5, and are also prime numbers.
    
    Args:
    numbers (list): A list of integers.
    
    Returns:
    list: A list of numbers that meet the specified conditions.
    """
    def is_prime(num):
        """
        Checks if a number is prime.
        
        Args:
        num (int): The number to check.
        
        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in numbers if num % 3 == 0 and num % 5 == 0 and is_prime(num)]