"""
QUESTION:
Write a function `check_even_numbers` that takes two integers `x` and `y` as input and checks the following conditions: 
- Both `x` and `y` are even numbers.
- `x` is equal to `y` and both are equal to 2.

The function should use bitwise operators to check if `x` and `y` are even numbers.
"""

def check_even_numbers(x, y):
    return (x & 1 == 0 and y & 1 == 0 and x == y == 2)