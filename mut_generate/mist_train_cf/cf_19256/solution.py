"""
QUESTION:
Write a function named `sum_of_squares_of_primes` that takes a list of integers as input and returns the sum of the squares of all prime numbers in the list that are not divisible by both 3 and 5. The function should not take any additional parameters other than the list of numbers.
"""

def sum_of_squares_of_primes(numbers):
    """
    Calculate the sum of the squares of all prime numbers in the list 
    that are not divisible by both 3 and 5.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        int: The sum of the squares of the prime numbers.
    """
    
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_divisible_by_3_and_5(n):
        """Check if a number is divisible by both 3 and 5."""
        return n % 3 == 0 and n % 5 == 0

    return sum([n**2 for n in numbers if is_prime(n) and not is_divisible_by_3_and_5(n)])