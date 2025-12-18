"""
QUESTION:
Create a function named `lcm(x: int, y: int, z: int)` to calculate the Least Common Multiple (LCM) of three integers. The function should use an efficient algorithm and handle the constraint that 1 <= x, y, z <= 10^9.
"""

def entance(x: int, y: int, z: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of three integers.
    
    The function uses the Euclidean algorithm to find the Greatest Common Divisor(GCD), 
    and then use the formula to find the LCM, lcm(a,b) = a*b / gcd(a,b).
    
    Parameters:
    x (int): The first number.
    y (int): The second number.
    z (int): The third number.
    
    Returns:
    int: The Least Common Multiple of x, y, and z.
    
    Raises:
    AssertionError: If any of the input numbers are not between 1 and 10^9.
    """
    
    assert 1 <= x <= 10**9 and 1 <= y <= 10**9 and 1 <= z <= 10**9, 'Input numbers should be between 1 and 10^9'
    
    def gcd(a: int, b: int) -> int:
        """
        Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
        
        Parameters:
        a (int): The first number.
        b (int): The second number.
        
        Returns:
        int: The Greatest Common Divisor of a and b.
        """
        while(b):
            a, b = b, a % b
        return a
    
    # Compute the lcm of x and y first
    lcm_xy = x * y // gcd(x, y)
    
    # Then compute the lcm of (x*y) and z
    return lcm_xy * z // gcd(lcm_xy, z)