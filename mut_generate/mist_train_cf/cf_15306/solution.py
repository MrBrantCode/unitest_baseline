"""
QUESTION:
Create a function `gcd(a, b)` that calculates the greatest common divisor of two input numbers `a` and `b` without using any built-in functions or modules that directly calculate the greatest common divisor. The function should have a time complexity of O(log(min(a,b))) and space complexity of O(1), where 'a' and 'b' are the input numbers.
"""

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    
    return a