"""
QUESTION:
Create a function called 'lcm' that calculates the Least Common Multiple (LCM) of two integers 'a' and 'b' and returns the result. The function should take two integers 'a' and 'b' as parameters and should be optimized for performance. The constraints are 1 <= a, b <= 10^6.
"""

def lcm(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) using the Euclidean algorithm.

    Constraints: 1 <= a, b <= 10^6
    """
    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a
    return a * b // gcd(a, b)