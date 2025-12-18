"""
QUESTION:
Write a function named `addNumbers` that takes two integers `x` and `y` as input and returns their sum using only bitwise operations (unary operators), without using the arithmetic addition operator (+).
"""

def add_numbers(x: int, y: int) -> int:
    """
    Adds two numbers using only bitwise operations.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.
    """
    while y != 0:
        # carry now contains common set bits of x and y
        carry = x & y
        
        # Sum of bits of x and y where at least one of the bits is not set
        x = x ^ y
        
        # Carry is shifted by one so that adding it to x gives the required sum
        y = carry << 1
    
    return x