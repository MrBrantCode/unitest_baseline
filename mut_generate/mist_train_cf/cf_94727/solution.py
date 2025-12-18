"""
QUESTION:
Write a function `multiply(b, c)` that multiplies two integers `b` and `c` without using the asterisk (*) operator, arithmetic operators (+, -, /), loops, or recursive function calls. The function should use only bitwise operators (&, |, ^, ~, <<, >>) and handle negative numbers. The time complexity should be O(log n), where n is the value of the smaller number between `b` and `c`.
"""

def multiply(b, c):
    if b == 0 or c == 0:
        return 0
    
    if b < 0:
        b = ~b + 1  # convert b to positive
    if c < 0:
        c = ~c + 1  # convert c to positive
    
    result = 0
    mask = 1
    
    while c != 0:
        if c & 1:
            result += b
        
        b <<= 1
        c >>= 1
        mask <<= 1
    
    if (b < 0) ^ (c < 0):  # if exactly one of b or c is negative
        result = ~result + 1  # convert result to negative
    
    return result