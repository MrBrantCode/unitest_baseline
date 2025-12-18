"""
QUESTION:
Write a function named `lcm` that calculates the least common multiple of two integers. The function should take two parameters, `a` and `b`, and return their least common multiple.
"""

def lcm(a, b):
    """Compute the least common multiple of a and b."""
    def gcd(a, b):
        """Compute the greatest common divisor of a and b."""
        while b != 0:
            a, b = b, a % b
        return a

    return a * b // gcd(a, b)