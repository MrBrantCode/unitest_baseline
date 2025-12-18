"""
QUESTION:
Implement a function `gcd(a: int, b: int) -> (int, int)` that calculates the Greatest Common Divisor (GCD) of two integers `a` and `b` using the most efficient algorithm possible. The function should also return the smallest possible sum of two integers that yields this GCD. The input integers `a` and `b` are constrained such that 1 <= a, b <= 10^9.
"""

def gcd(a: int, b: int) -> (int, int):
    """
    Compute the GCD of a and b through a maximally efficient algorithm.
    Also compute the smallest possible sum of two numbers that yields this GCD.

    Constraints: 1 <= a, b <= 10^9 
    """

    if a == b:
        return a, 2 * a

    elif a == 0:
        return b, 2 * b

    elif b == 0:
        return a, 2 * a

    shift = 0
    while ((a | b) & 1) == 0:
        shift += 1
        a >>= 1
        b >>= 1

    while (a & 1) == 0:
        a >>= 1

    while b != 0:
        while (b & 1) == 0:
            b >>= 1

        if a > b:
            a, b = b, a

        b = b - a

    return a << shift, (a << shift) * 2