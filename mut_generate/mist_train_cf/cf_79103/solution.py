"""
QUESTION:
Write a function named `optimized_lcm` that takes three integers as input and returns the least common multiple (LCM) of the three numbers along with the number of iterations used to calculate the LCM. The function should use an optimized algorithm to reduce the number of iterations, such as utilizing the greatest common divisor (GCD) of the numbers. The function should be efficient for large inputs (up to 1,000,000).
"""

def optimized_lcm(x, y, z):
    """Calculate the least common multiple (LCM) of three numbers using the greatest common divisor (GCD)."""
    
    def gcd(a, b):
        """Calculate the Greatest Common Divisor of a and b."""
        gcd_count = 0
        while b:
            a, b = b, a % b
            gcd_count += 1
        return a, gcd_count

    gcd_xy, gcd_count_xy = gcd(x, y)
    lcm_xy = x * y // gcd_xy
    gcd_xyz, gcd_count_xyz = gcd(lcm_xy, z)
    lcm_xyz = lcm_xy * z // gcd_xyz
    return lcm_xyz, gcd_count_xy + gcd_count_xyz