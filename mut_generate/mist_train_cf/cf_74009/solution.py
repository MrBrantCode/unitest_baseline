"""
QUESTION:
Write a function to calculate the least common multiple (LCM) of three integers. The function should use a helper function to calculate the greatest common divisor (GCD) of two integers. The GCD function should use the Euclidean algorithm. The LCM function should use the formula lcm(a, b) = abs(a*b) // gcd(a, b). The input integers will be provided by the user.
"""

def gcd(x, y):
    """Calculate the greatest common divisor of two integers using the Euclidean algorithm."""
    while y:
        x, y = y, x % y
    return x

def lcm_of_three(a, b, c):
    """Calculate the least common multiple of three integers."""
    def lcm(x, y):
        """Calculate the least common multiple of two integers using the formula lcm(a, b) = abs(a*b) // gcd(a, b)."""
        return abs(x*y) // gcd(x, y)
    
    return lcm(lcm(a, b), c)