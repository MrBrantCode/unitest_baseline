"""
QUESTION:
Design a function named `calculate_gcd` that takes two integers `a` and `b` as input, calculates their greatest common divisor (GCD) using the Euclidean algorithm, and returns the result. The function should handle negative input numbers by returning their positive GCD. The implementation must not use any built-in GCD functions or libraries and should have a time complexity of O(log(min(a, b))).
"""

def calculate_gcd(a, b):
    # Convert negative numbers to positive
    a = abs(a)
    b = abs(b)

    # Base cases
    if a == 0:
        return b
    if b == 0:
        return a

    # Reduce larger number to smaller number
    if a > b:
        a, b = b, a

    # Apply Euclidean algorithm
    while b % a != 0:
        remainder = b % a
        b = a
        a = remainder

    return a