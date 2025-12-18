"""
QUESTION:
Write a function called `find_lcm` that takes two distinct whole numbers as input and returns their least common multiple. Use the Euclidean algorithm to find the Greatest Common Divisor (GCD) and then use this GCD to calculate the Least Common Multiple (LCM).
"""

def find_lcm(a, b):
    """
    This function takes two distinct whole numbers as input and returns their least common multiple.
    
    Parameters:
    a (int): The first whole number.
    b (int): The second whole number.
    
    Returns:
    int: The least common multiple of a and b.
    """
    gcd = math.gcd(a, b)
    lcm = abs(a*b) // gcd
    return lcm