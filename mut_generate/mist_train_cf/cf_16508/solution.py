"""
QUESTION:
Write a Python function called `is_prime(number)` to check if a given number is prime. A number is prime if it is greater than 1 and has no divisors other than 1 and itself. Implement the function to return `True` if the number is prime and `False` otherwise, and optimize it to exit early if a divisor is found. Use this function to calculate the average of prime numbers in a given list, excluding non-prime numbers from the calculation.
"""

def is_prime(number):
    """
    Checks if a given number is prime.
    
    A number is prime if it is greater than 1 and has no divisors other than 1 and itself.
    
    Args:
        number (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True