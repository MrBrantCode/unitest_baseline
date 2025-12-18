"""
QUESTION:
Create a function called `is_power_of_three` that determines whether a given integer `n` is a power of three. The function should return `True` if `n` is a power of three, and `False` otherwise. The function should work with positive integers and return `False` for non-positive integers.
"""

def is_power_of_three(n: int) -> bool:
    """
    This function determines whether a given integer n is a power of three.
    
    Args:
    n (int): The input integer to be checked.
    
    Returns:
    bool: True if n is a power of three, False otherwise.
    """
    
    # If n is less than or equal to 0, it's not a power of three
    if n <= 0:
        return False
    
    # Keep dividing n by 3 as long as it's divisible evenly
    while n % 3 == 0:
        n /= 3
    
    # If n becomes 1, it's a power of three
    return n == 1