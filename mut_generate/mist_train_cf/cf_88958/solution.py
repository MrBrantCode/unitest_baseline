"""
QUESTION:
Write a function `gcd(n1, n2)` that calculates the greatest common divisor (GCD) of two numbers `n1` and `n2` and returns the GCD along with the coefficients `x` and `y` such that `n1 * x + n2 * y = GCD(n1, n2)`. The function should have a time complexity of O(log(min(n1, n2))) and a space complexity of O(1). The input numbers `n1` and `n2` can be positive or negative, and the function should not use any built-in Python functions or libraries for calculating the GCD.
"""

def gcd(n1, n2):
    def gcd_extended(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = gcd_extended(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

    n1 = abs(n1)
    n2 = abs(n2)
    if n2 == 0:
        return n1, 1, 0
    
    gcd, x, y = gcd_extended(n1, n2)
    
    if n1 == abs(n1):
        x *= 1
    else:
        x *= -1
    if n2 == abs(n2):
        y *= 1
    else:
        y *= -1
    
    return gcd, x, y