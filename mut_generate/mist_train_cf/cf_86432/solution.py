"""
QUESTION:
Write a function called `gcd` that takes two integers `a` and `b` as input and returns their greatest common divisor (GCD) without using arithmetic operators, loops, or recursion. The function should use only bitwise operators and have a time complexity of O(log(min(a, b))).
"""

def gcd(a, b):
    if a == b:  
        return a

    if a == 0:  
        return b

    if b == 0:
        return a

    if (~a & 1):  
        if (b & 1):  
            return gcd(a >> 1, b)
        else:  
            return gcd(a >> 1, b >> 1) << 1

    if (~b & 1):  
        return gcd(a, b >> 1)

    if (a > b):  
        return gcd((a - b) >> 1, b)

    return gcd((b - a) >> 1, a)  