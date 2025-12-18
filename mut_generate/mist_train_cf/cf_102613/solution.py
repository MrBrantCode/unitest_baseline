"""
QUESTION:
Create a function named `gcd` that takes two integer parameters, `a` and `b`, and returns their greatest common divisor without using any built-in functions or modules that directly calculate the greatest common divisor.
"""

def gcd(a, b):
    # Ensure a is greater than or equal to b
    if a < b:
        a, b = b, a
    
    # Euclidean algorithm
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    
    return a