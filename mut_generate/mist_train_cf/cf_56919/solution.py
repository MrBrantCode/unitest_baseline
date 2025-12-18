"""
QUESTION:
Implement a function `lcm(x: int, y: int, z: int) -> int` to compute the Least Common Multiple (LCM) of three distinct numbers x, y, and z. The function should operate within the following constraints: 1 <= x, y, z <= 10^9.
"""

def lcm(x: int, y: int, z: int) -> int:
    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    lcm_xy = (x * y) // gcd(x, y)
    return lcm_xy * z // gcd(lcm_xy, z)