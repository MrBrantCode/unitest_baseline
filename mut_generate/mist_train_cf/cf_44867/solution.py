"""
QUESTION:
Write a function named `findNumbers(a, b)` that takes two integers as input and returns a tuple containing their least common multiple (LCM) and greatest common divisor (GCD) in that order. The function should include error checking to handle cases where the inputs are not both positive integers, and it should return an error message in such cases.
"""

def findNumbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Both inputs must be integers"
    if a<=0 or b<=0: 
        return "Both inputs must be positive integers"

    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    gcd_value = gcd(a, b)
    lcm_value = abs(a*b) // gcd_value  
    return (lcm_value, gcd_value)