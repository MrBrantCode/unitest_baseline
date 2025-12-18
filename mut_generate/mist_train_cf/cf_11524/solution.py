"""
QUESTION:
Write a function `gcd` that takes two non-negative integers `a` and `b` as input and returns their greatest common divisor without using any built-in mathematical functions or libraries. The function should handle cases where one or both of the input integers are 0.
"""

def entance(a, b):
    # Base case: if one of the numbers is 0, the other number is the GCD
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Subtract the smaller number from the larger number
    if a > b:
        return entance(a - b, b)
    else:
        return entance(a, b - a)