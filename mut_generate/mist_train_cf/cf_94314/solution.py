"""
QUESTION:
Implement a function `add_numbers(x, y)` that adds two integers `x` and `y` using only bitwise operators. The function should not use the addition operator.
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