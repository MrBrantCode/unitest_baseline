"""
QUESTION:
Implement a function `add_numbers(a, b)` that takes two integers `a` and `b` as input and returns their sum without using any arithmetic operators or built-in functions specifically designed for addition.
"""

def add_numbers(a, b):
    while b != 0:
        # Calculate the carry
        carry = a & b
        
        # Perform the addition
        a = a ^ b
        
        # Shift the carry by 1 bit to the left
        b = carry << 1
    
    return a