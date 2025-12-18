"""
QUESTION:
Create a function `check_even_odd(n)` that determines whether a given integer `n` is even or odd without using any arithmetic operators. The function should take an integer `n` as input and output whether the number is even or odd.
"""

def check_even_odd(n):
    # Check if the least significant bit in binary is 0
    if n & 1:
        return f"{n} is odd."
    else:
        return f"{n} is even."