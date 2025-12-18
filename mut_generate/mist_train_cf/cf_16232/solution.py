"""
QUESTION:
Create a function `isMultiplePrime(x)` that takes an integer `x` as input and returns a boolean value. The function should return `True` if `x` is a multiple of five, greater than or equal to 25, and a prime number. Otherwise, it should return `False`.
"""

def isMultiplePrime(x):
    """
    Checks if a number is a multiple of five, greater than or equal to 25, and a prime number.
    
    Args:
        x (int): The input number.
    
    Returns:
        bool: True if the number is a multiple of five, greater than or equal to 25, and a prime number. False otherwise.
    """
    if x % 5 == 0 and x >= 25:
        # Check if x is a prime number
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False  # x is not a prime number
        return True  # x is a prime number
    return False  # x does not satisfy all conditions