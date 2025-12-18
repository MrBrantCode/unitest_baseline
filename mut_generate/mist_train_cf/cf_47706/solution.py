"""
QUESTION:
Write a function `gcd(a: int, b: int) -> int` that calculates the Greatest Common Divisor (GCD) of two integers `a` and `b`. The function should use an efficient strategy to compute the GCD and handle cases where `1 <= a, b <= 10^9`.
"""

def entance(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a