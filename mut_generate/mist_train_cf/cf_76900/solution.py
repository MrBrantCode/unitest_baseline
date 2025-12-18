"""
QUESTION:
Create a function called `add_numbers` that takes two integers `a` and `b` as input and returns their sum using only bitwise operators. The function should not use the '+' operator for addition. The input numbers are represented in binary form and the function should handle carry-over values in the addition process.
"""

def add_numbers(a, b):
    while(b!=0):
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a