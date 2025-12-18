"""
QUESTION:
Implement a function "add" in a class that takes two integers as input and returns their sum without using arithmetic operators (+, -, *, /). The solution should only utilize bitwise and logical operations.
"""

def add(a: int, b: int) -> int:
    """
    This function calculates the sum of two integers without using arithmetic operators.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The sum of a and b.
    """
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a