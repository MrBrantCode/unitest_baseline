"""
QUESTION:
Write a function `gcd(a, b)` that calculates the greatest common divisor of two numbers `a` and `b` without using built-in functions or modules that directly calculate the greatest common divisor. The function should have a time complexity of O(log(min(a, b))) and space complexity of O(1), handle negative input numbers correctly, and return the greatest common divisor as a positive integer.
"""

def gcd(a, b):
    # convert negative numbers to positive
    a = abs(a)
    b = abs(b)
    
    # base cases
    if a == 0:
        return b
    if b == 0:
        return a
    
    # find the GCD
    while b != 0:
        temp = b
        b = a % b
        a = temp
    
    return a