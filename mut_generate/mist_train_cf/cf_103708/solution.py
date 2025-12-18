"""
QUESTION:
Create a function `gcd(a, b, c)` that calculates the greatest common divisor (GCD) of three numbers `a`, `b`, and `c`. The function should return the GCD of the three numbers.
"""

def gcd(a, b, c):
    """
    Calculate the greatest common divisor (GCD) of three numbers a, b, and c.
    
    Args:
        a (int): The first number.
        b (int): The second number.
        c (int): The third number.
    
    Returns:
        int: The GCD of a, b, and c.
    """
    # Calculate the GCD of a and b first
    while b:
        a, b = b, a % b
    
    # Calculate the GCD of the result and c
    while c:
        a, c = c, a % c
    
    return a