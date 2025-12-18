"""
QUESTION:
Write a function named `check_prime_in_array` that takes a list `array` as an argument and returns `True` if all elements at prime indices in the array are prime numbers, and `False` otherwise. Note that prime indices start from 2.
"""

def is_prime(n): 
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for current in range(3, int(n ** 0.5) + 1, 2): 
        if n % current == 0: 
            return False
    return True

def check_prime_in_array(array):
    """Return True if all elements at prime indices in the array are prime numbers."""
    return all(is_prime(array[i]) for i in range(2, len(array)) if is_prime(i))