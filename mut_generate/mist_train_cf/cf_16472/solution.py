"""
QUESTION:
Create a function named `gcd` that calculates the Greatest Common Denominator of two numbers `a` and `b`. The function should not use any built-in mathematical functions or libraries for calculating the GCD. It should have a time complexity of O(log(min(a, b))) and a space complexity of O(1).
"""

def entance(a, b):
    if a < b:
        a, b = b, a # Swap numbers if a < b
        
    def gcd(x, y):
        if y == 0:
            return x
        return gcd(y, x % y)
    
    return gcd(a, b)