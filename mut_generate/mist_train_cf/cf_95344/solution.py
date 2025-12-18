"""
QUESTION:
Implement the `calculate_gcd` function to calculate the greatest common divisor (GCD) of two integers `a` and `b` using the Euclidean algorithm, without using any built-in GCD functions or libraries. The function must have a time complexity of O(log(min(a, b))) and handle negative inputs by returning the positive GCD.
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