"""
QUESTION:
Develop a function `optimal_lcm(x, y, z)` that calculates the smallest common multiple (LCM) of three distinct numbers `x`, `y`, and `z`. The function should use an efficient algorithm to compute the LCM and handle cases where `1 <= x, y, z <= 10^9`.
"""

def gcd(a, b):
    """Calculate the Greatest Common Divisor of two numbers using Euclidean algorithm."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def optimal_lcm(x: int, y: int, z: int) -> int:
    """Calculate the Least Common Multiple (LCM) of three distinct numbers."""
    lcm_ab = (x * y) // gcd(x, y)
    lcm_abc = (lcm_ab * z) // gcd(lcm_ab, z)
    return lcm_abc