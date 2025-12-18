"""
QUESTION:
Create a function named `add_numbers` that takes two integers `a` and `b` as input parameters and returns their sum without using any arithmetic operators (+, -, *, /). The function should use recursion and bitwise operations to calculate the sum.
"""

def add_numbers(a, b):
    if b == 0:
        return a
    else:
        # XOR operation gives the sum without carrying
        sum_without_carry = a ^ b
        
        # AND operation followed by left shift gives the carry
        carry = (a & b) << 1
        
        # Recursively call add_numbers with the sum and carry
        return add_numbers(sum_without_carry, carry)