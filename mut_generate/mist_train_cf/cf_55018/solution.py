"""
QUESTION:
Create a function called `get_gcd(x, y)` that takes two integers as input and returns their greatest common divisor (GCD) without using built-in GCD functions or libraries. The function should first check if either number is negative, in which case it should return an error message. Otherwise, it should calculate the GCD by finding the intersection of the factors of both numbers and returning the maximum value from this intersection.
"""

def get_gcd(x, y):
    """
    This function calculates the greatest common divisor (GCD) of two numbers.
    
    Args:
    x (int): The first number.
    y (int): The second number.
    
    Returns:
    int or str: The GCD of x and y if both are non-negative, otherwise an error message.
    """
    
    # Check if either number is negative
    if x < 0 or y < 0:
        return "Error: Negative numbers not allowed."
    
    # Calculate factors of x and y
    factors_x = [i for i in range(1, x + 1) if x % i == 0]
    factors_y = [i for i in range(1, y + 1) if y % i == 0]
    
    # Find the intersection of factors
    intersect = set(factors_x) & set(factors_y)
    
    # Return the maximum value from the intersection (GCD)
    return max(intersect)