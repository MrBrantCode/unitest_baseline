"""
QUESTION:
Write a function `is_prime_number(num)` that takes an integer `num` as input and returns `True` if `num` is a prime number, and `False` otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should not use any external libraries or pre-computed values.
"""

def is_prime_number(num):
    '''
    This algorithm checks if a given number is a prime number or not.
    
    Args:
    num (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    '''
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True