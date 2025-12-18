"""
QUESTION:
Write two functions, `gcd(a, b)` and `lcm(a, b)`, to calculate the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of two given integers `a` and `b`. The GCD is the maximum common factor that can divide both numbers without leaving a remainder, while the LCM is the smallest multiple that is evenly divisible by both numbers. The `gcd` function should use the Euclidean algorithm, and the `lcm` function should use the formula `lcm(a, b) = abs(a*b) / gcd(a, b)`.
"""

def entance(a, b):
    """
    Function to calculate Greatest Common Divisor (GCD) and Lowest Common Multiple (LCM)
    """
    def gcd(a, b):
        """
        Helper function to calculate Greatest Common Divisor (GCD)
        """
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(a, b):
        """
        Helper function to calculate Lowest Common Multiple (LCM)
        """
        return abs(a*b) // gcd(a, b)

    return gcd(a, b), lcm(a, b)