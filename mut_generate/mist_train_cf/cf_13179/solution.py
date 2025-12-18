"""
QUESTION:
Write a function `add_numbers` that takes two integers `a` and `b` as input and returns their sum without using any arithmetic operators such as +, -, *, or /. The function should only use bitwise operations.
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