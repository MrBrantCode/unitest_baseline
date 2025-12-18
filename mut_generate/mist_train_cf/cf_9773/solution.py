"""
QUESTION:
Create a function called `gcd(a, b)` that takes two integers as input and returns their greatest common divisor using the Euclidean algorithm. The function should ensure that it works regardless of the order of the input integers.
"""

def gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        remainder = a % b
        a, b = b, remainder
    
    return a