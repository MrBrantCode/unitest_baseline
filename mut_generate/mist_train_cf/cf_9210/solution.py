"""
QUESTION:
Write a function called `gcd_quotient` that takes two integers as input and returns the quotient obtained by dividing the smaller number by the greatest common divisor of the two numbers. The function should not take any other parameters.
"""

def gcd_quotient(a, b):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    return min(a, b) // gcd(a, b)