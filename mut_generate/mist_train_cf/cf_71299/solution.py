"""
QUESTION:
Write a function `lcm(x: int, y: int, z: int) -> int` that calculates the Least Common Multiple (LCM) of three numbers (x, y, and z) using an optimized algorithm. The function should take three integers as input and return their LCM. The constraints are 1 <= x, y, z <= 10^9.
"""

def lcm(x: int, y: int, z: int) -> int:
    """
    Ascertain the LCM of x, y, and z using a resource-efficient technique.

    Constraints: 1 <= x, y, z <= 10^9
    """
    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    lcm_two = (x * y) // gcd(x, y)
    return (lcm_two * z) // gcd(lcm_two, z)