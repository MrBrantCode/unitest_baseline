"""
QUESTION:
Write a function named `multiply` that takes two integers `b` and `c` and returns their product without using the asterisk (*) operator or any arithmetic operators (+, -, /). The function should only use bitwise operators (&, |, ^, ~, <<, >>) and must handle negative numbers. The time complexity of the function should be O(log n), where n is the value of the smaller number between `b` and `c`. The function should not use any intermediate variables, loop structures, or recursive function calls.
"""

def multiply(b, c):
    if b == 0 or c == 0:
        return 0
    
    if b < 0:
        b = ~b + 1  
    if c < 0:
        c = ~c + 1  
    
    result = 0
    mask = 1
    
    while c != 0:
        if c & 1:
            result += b
        
        b <<= 1
        c >>= 1
        mask <<= 1
    
    if (b < 0) ^ (c < 0):  
        result = ~result + 1  
    
    return result