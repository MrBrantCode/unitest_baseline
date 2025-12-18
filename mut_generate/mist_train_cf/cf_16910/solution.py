"""
QUESTION:
Create a function named `add_numbers` that takes two integers as input and returns their sum without using any arithmetic operators or built-in addition functions. The function should use bitwise operations to achieve this.
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