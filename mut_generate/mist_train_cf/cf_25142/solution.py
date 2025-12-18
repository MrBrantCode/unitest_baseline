"""
QUESTION:
Write a function named `is_prime` that takes an integer `n` as input and returns a boolean indicating whether the number is prime or not. The function should return `False` for numbers less than or equal to 1, and `True` if the number is only divisible by 1 and itself.
"""

def is_prime(n):
    """This function will check if a number is a prime number or not."""
    # Corner case 
    if n <= 1: 
        return False

    # Check from 2 to n-1 
    for i in range(2,n): 
        if n % i == 0: 
            return False
    return True