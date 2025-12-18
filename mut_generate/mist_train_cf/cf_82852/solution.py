"""
QUESTION:
Create a function named `gcd` that takes two positive integers as input and returns their greatest common divisor (GCD) using the Euclidean algorithm. The function should first verify that both input integers are positive and return an error message if either integer is negative. The GCD should be calculated using the Euclidean method, which replaces `a` with `b` and `b` with `a % b` until `b` becomes `0`, at which point `a` is the GCD.
"""

def gcd(a, b):
    if a < 0 or b < 0:
        return "Error: the provided integers must be positive."
    else:
        while b != 0:
            a, b = b, a % b
        return a