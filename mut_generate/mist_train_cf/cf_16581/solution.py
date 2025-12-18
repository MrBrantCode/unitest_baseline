"""
QUESTION:
Implement a function `add_numbers(x, y)` that adds two numbers without using the addition operator. The function should only use bitwise operators.
"""

def add_numbers(x, y):
    while y != 0:
        # Calculate the carry
        carry = x & y
        
        # Perform the addition without carry
        x = x ^ y
        
        # Left shift the carry by 1 to add it to the next bit
        y = carry << 1
    
    return x