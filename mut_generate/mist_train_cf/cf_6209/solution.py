"""
QUESTION:
Implement a function `add_without_arithmetic(a, b)` that takes two integers `a` and `b` as input and returns their sum. The function must only use bitwise operators (AND, OR, XOR, NOT), shift operators (left shift, right shift), and control flow statements (if-else, for loop, while loop) without using any arithmetic operators (+, -, *, /).
"""

def add_without_arithmetic(a, b):
    while b != 0:
        # Calculate the carry using bitwise AND and left shift
        carry = a & b
        carry = carry << 1

        # Calculate the sum using bitwise XOR
        a = a ^ b

        # Update the value of b to be the carry
        b = carry

    return a