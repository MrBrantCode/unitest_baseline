"""
QUESTION:
Write a function `gcd(a, b)` that calculates the greatest common divisor of two given integers `a` and `b` using only bitwise operators, without using any arithmetic operators, loops, or recursion. The function should have a time complexity of O(log(min(a, b))).
"""

def entance(a, b):
    if a == b:  
        return a

    if a == 0:  
        return b

    if b == 0:
        return a

    if (~a & 1):  
        if (b & 1):  
            return entance(a >> 1, b)
        else:  
            return entance(a >> 1, b >> 1) << 1

    if (~b & 1):  
        return entance(a, b >> 1)

    if (a > b):  
        return entance((a - b) >> 1, b)

    return entance((b - a) >> 1, a)  