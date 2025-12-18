"""
QUESTION:
Write a function `is_prime` that checks whether a given integer is a prime number or not. The function should return `True` if the number is prime and `False` otherwise. The function should be efficient for large inputs. Assume the input number is a positive integer.
"""

def is_prime(num):
    """
    Checks whether a given integer is a prime number or not.
    
    Args:
    num (int): A positive integer to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num > 1:  
        for i in range(2, int(num**0.5) + 1):  
            if (num % i) == 0:  
                return False
        return True
    else:
        return False