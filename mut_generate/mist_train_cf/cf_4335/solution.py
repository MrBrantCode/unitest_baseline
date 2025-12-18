"""
QUESTION:
Write a function named `multiply` that takes two positive integers `a` and `b` as input and returns their product without using the multiplication operator, division operator, or modulo operator. The time complexity should be less than O(n^2) and the space complexity should be less than O(n), where n is the number of bits in the binary representation of the larger number.
"""

def multiply(a, b):
    result = 0

    while b:
        if b & 1:
            result += a
        
        a <<= 1
        b >>= 1
    
    return result